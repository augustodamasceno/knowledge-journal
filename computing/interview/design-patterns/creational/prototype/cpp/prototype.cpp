#include <iostream>
#include <memory>
#include <string>
#include <unordered_map>

class DiagramNode {
public:
    explicit DiagramNode(std::string label) : label_(std::move(label)) {}
    virtual ~DiagramNode() = default;

    virtual std::unique_ptr<DiagramNode> clone() const = 0;
    virtual void render() const = 0;

protected:
    std::string label_;
};

class CircleNode : public DiagramNode {
public:
    CircleNode(std::string label, double radius)
        : DiagramNode(std::move(label)), radius_(radius) {}

    std::unique_ptr<DiagramNode> clone() const override {
        return std::make_unique<CircleNode>(*this);
    }

    void render() const override {
        std::cout << "Circle(" << label_ << ", r=" << radius_ << ")\n";
    }

private:
    double radius_;
};

class RectangleNode : public DiagramNode {
public:
    RectangleNode(std::string label, double width, double height)
        : DiagramNode(std::move(label)), width_(width), height_(height) {}

    std::unique_ptr<DiagramNode> clone() const override {
        return std::make_unique<RectangleNode>(*this);
    }

    void render() const override {
        std::cout << "Rectangle(" << label_ << ", " << width_ << "x" << height_ << ")\n";
    }

private:
    double width_;
    double height_;
};

class PrototypeRegistry {
public:
    void register_node(const std::string& name, std::unique_ptr<DiagramNode> prototype) {
        prototypes_[name] = std::move(prototype);
    }

    std::unique_ptr<DiagramNode> create(const std::string& name) const {
        auto it = prototypes_.find(name);
        if (it == prototypes_.end()) {
            throw std::runtime_error("Prototype not found");
        }
        return it->second->clone();
    }

private:
    std::unordered_map<std::string, std::unique_ptr<DiagramNode>> prototypes_;
};

int main() {
    PrototypeRegistry registry;
    registry.register_node("small_circle", std::make_unique<CircleNode>("Small", 1.0));
    registry.register_node("wide_rect", std::make_unique<RectangleNode>("Wide", 3.0, 1.0));

    auto node1 = registry.create("small_circle");
    auto node2 = registry.create("wide_rect");

    node1->render();
    node2->render();
}
