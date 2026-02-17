# fpga
Field-Programmable Gate Array (FPGA) [[1]](https://www.ibm.com/think/topics/field-programmable-gate-arrays) Notes and Implementations.  

## 1. Software Stack  

### 1.1 AMD/Xilinx New Kits with Matlab  
* Windows 11  
* Vivado 2025.1  [[3]](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/2025-1.html)
* Matlab 2024a  
* Open Matlab loading toolbox, then Simulink and Use AMD Toolbox  

### 1.2 Xilinx Old Kits with Matlab  
* Windows 10  
* Vitis Model Composer  
* ISE 14.3   
* Matlab 2012b  
* Open Matlab, Simulink and use Xilinx Toolboxes  

### 1.3 Amazon EC2 F2 FPGA Instances
* FPGA Developer AMI (Amazon Linux 2) [[7]](https://aws.amazon.com/marketplace/pp/prodview-f5kjsenkfkz5u) - Pre-configured Amazon Machine Image with development tools for FPGA design, including simulation and compilation environments.
* Xilinx Vivado Design Suite (included in AMI) - Comprehensive software for FPGA synthesis, implementation, and debugging at no additional cost.
* AWS FPGA Development Kit [[6]](https://github.com/aws/aws-fpga) - Open-source kit providing scripts, documentation, and interfaces for custom hardware development and C/C++/OpenCL acceleration.
* AWS CLI - Command-line interface for managing AWS resources, deploying FPGA images, and interacting with EC2 services.

### 1.4 Vivado ML Free Version

The AMD Vivado™ Design Suite: Standard Edition is available for free and provides access to essential FPGA design tools and features. This edition supports a limited set of devices but includes key capabilities such as Vivado IP Integrator, Dynamic Function eXchange, Vitis High-Level Synthesis, Vivado Simulator, Device Programmer, Logic Analyzer, Serial I/O Analyzer, and more.

**Download Vivado ML Standard Edition for free:** [https://www.amd.com/pt/products/software/adaptive-socs-and-fpgas/vivado/vivado-buy.html](https://www.amd.com/pt/products/software/adaptive-socs-and-fpgas/vivado/vivado-buy.html)

For more details and supported devices, visit the [official Vivado download page](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools.html).

## 2. Books

### 2.1 SystemVerilog

#### 2.1.1 Design (Synthesizable RTL)
[1] S. Sutherland, S. Davidmann, and P. Flake, *SystemVerilog for Design: A Guide to Using SystemVerilog for Hardware Design and Modeling*, 2nd ed. New York, NY, USA: Springer, 2006.  
    * Focus: Distinguishes synthesizable logic from simulation constructs to prevent common hardware compilation errors.

<img src="https://m.media-amazon.com/images/I/71iHCwVf5eL._SY425_.jpg" alt="SystemVerilog for Design" height="120"/>

[2] P. P. Chu, *FPGA Prototyping by SystemVerilog Examples: Xilinx MicroBlaze MCS SoC Edition*. Hoboken, NJ, USA: Wiley, 2018.  
    * Focus: Provides practical "cookbook" examples for Xilinx FPGAs, including IP core integration and embedded SoC design.

<img src="https://m.media-amazon.com/images/I/71TyyhjptgL._SY425_.jpg" alt="FPGA Prototyping by SystemVerilog Examples" height="120"/>

#### 2.1.2 Verification (Simulation & Testbenches)
[3] C. Spear and G. Tumbush, *SystemVerilog for Verification: A Guide to Learning the Testbench Language Features*, 3rd ed. New York, NY, USA: Springer, 2012.  
    * Focus: Teaches object-oriented programming (OOP) and class-based testbenches for robust design verification.

<img src="https://m.media-amazon.com/images/I/61hY5a-bBuL._SY425_.jpg" alt="SystemVerilog for Verification" height="120"/>

[4] R. Salemi, *The UVM Primer: An Introduction to the Universal Verification Methodology*. Boston, MA, USA: Boston Light Press, 2013.  
    * Focus: Serves as an accessible introduction to UVM concepts for building advanced industry-standard verification environments.

<img src="https://m.media-amazon.com/images/I/51O+zWqJnZL._SY385_.jpg" alt="The UVM Primer" height="120"/>

### 2.2 VHDL

#### 2.2.1 Design (Synthesizable RTL)
[1] P. J. Ashenden, *The Designer's Guide to VHDL*, 3rd ed. San Francisco, CA, USA: Morgan Kaufmann, 2008.  
    * Focus: Comprehensive reference for VHDL syntax, semantics, and best practices for synthesizable design.

<img src="https://m.media-amazon.com/images/I/41jIxAyrSOL._SX342_SY445_FMwebp_.jpg" alt="The Designer's Guide to VHDL" height="120"/>

[2] D. R. Smith and P. D. Franzon, *VHDL for Programmable Logic*, 2nd ed. Boston, MA, USA: Springer, 2010.  
    * Focus: Practical VHDL design examples for FPGAs and CPLDs, including testbenches and simulation.

<img src="https://m.media-amazon.com/images/I/51N7JW7ZJ4L._SX342_SY445_ControlCacheEqualizer_.jpg" alt="VHDL for Programmable Logic" height="120"/>

#### 2.2.2 Verification (Simulation & Testbenches)
[3] J. Bhasker, *A VHDL Primer*, 3rd ed. Upper Saddle River, NJ, USA: Prentice Hall, 1999.  
    * Focus: Introductory guide to VHDL for simulation, testbench creation, and verification techniques.

<img src="https://m.media-amazon.com/images/I/81MBdhHCqQL._SY425_.jpg" alt="A VHDL Primer" height="120"/>

[4] C. H. Roth Jr. and L. L. Kinney, *VHDL: Hardware Description and Design*, 2nd ed. Boston, MA, USA: Cengage Learning, 2010.  
    * Focus: Covers VHDL for both design and verification, with practical examples and exercises.

<img src="https://m.media-amazon.com/images/I/61wdMEqUfvL._SY466_.jpg" alt="VHDL: Hardware Description and Design" height="120"/>

### 2.3 Digital Signal and Image Processing

[1] R. Woods, J. McAllister, B. Bardak, G. Lightbody, *FPGA-Based Implementation of Signal and Data Processing*, 1st ed. Chichester, UK: Wiley, 2017.  
    * Focus: Practical approaches to implementing digital signal and data processing algorithms on FPGAs, with real-world examples and case studies.

<img src="https://m.media-amazon.com/images/I/51LguW0H26L._SY445_SX342_FMwebp_.jpg" alt="FPGA-Based Implementation of Signal and Data Processing" height="120"/>

### 2.4 Parallel Programming and HLS

[1] R. Kastner, J. Matai, S. Neuendorffer, *Parallel Programming for FPGAs: The HLS Book*, 1st ed. 2022.  
    * Focus: High-Level Synthesis (HLS) techniques and parallel programming models for FPGA development, including C/C++ and OpenCL.
> Download: https://arxiv.org/abs/1805.03648

<img src="https://kastner.ucsd.edu/wp-content/uploads/2018/03/admin/hls_book_cover.jpg" alt="Parallel Programming for FPGAs: The HLS Book" height="120"/>

[2] D. Pellerin and S. Thibault, *Practical FPGA Programming in C*, 1st ed. Upper Saddle River, NJ, USA: Prentice Hall, 2005.  
    * Focus: Using C programming for FPGA design, including high-level synthesis (HLS) techniques, algorithm mapping, and optimization for hardware implementation.

<img src="https://m.media-amazon.com/images/I/51z-t6f8V7L._SY445_SX342_FMwebp_.jpg" alt="Practical FPGA Programming in C" height="120"/>

[3] P. Coussy and A. Morawiec, *High-Level Synthesis: From Algorithm to Digital Circuit*, 1st ed. Dordrecht, Netherlands: Springer, 2008.  
    * Focus: Detailed exploration of high-level synthesis (HLS) processes, transforming C/C++/SystemC algorithms into efficient FPGA circuits, with optimization strategies.

<img src="https://m.media-amazon.com/images/I/41j47HoKlcL._SY445_SX342_FMwebp_.jpg" alt="High-Level Synthesis: From Algorithm to Digital Circuit" height="120"/>

### 2.5 Signals and Communication Technology

[1] U. Meyer-Baese, *Digital Signal Processing with Field Programmable Gate Arrays*, 5th ed. Cham, Switzerland: Springer, 2021.  
    * Focus: Comprehensive coverage of digital signal processing (DSP) techniques and their efficient implementation on FPGAs, with applications in communications and signal technology.

<img src="https://m.media-amazon.com/images/I/411ItqvjkiL._SY445_SX342_FMwebp_.jpg" alt="Digital Signal Processing with Field Programmable Gate Arrays" height="120"/>

### 2.6 General FPGA Design and Implementation

[1] P. Simpson, *FPGA Design: Best Practices for Team-based Design*, 1st ed. Cham, Switzerland: Springer, 2015.  
    * Focus: Comprehensive guide to FPGA design methodologies, emphasizing team collaboration, design reuse, and best practices for implementation and verification in complex projects.

<img src="https://m.media-amazon.com/images/I/41BA7gkvQTL._SY445_SX342_QL70_FMwebp_.jpg" alt="FPGA Design: Best Practices for Team-based Design" height="120"/>

[2] J. O. Hamblen, T. S. Hall, M. D. Furman, *Rapid Prototyping of Digital Systems: A Tutorial Approach*, 1st ed. New York, NY, USA: Springer, 2008.  
    * Focus: Tutorial-based introduction to FPGA prototyping, covering design entry, simulation, synthesis, and implementation using VHDL and Verilog with practical examples.

<img src="https://m.media-amazon.com/images/I/41CPyhpwSaL._SY445_SX342_FMwebp_.jpg" alt="Rapid Prototyping of Digital Systems: A Tutorial Approach" height="120"/>

### 2.7 FPGA Verification Methodologies

[1] A. Meyer, *Principles of Functional Verification*, 1st ed. Amsterdam, Netherlands: Elsevier, 2003.  
    * Focus: Methodologies for functional verification of digital designs, including simulation, formal methods, and testbench development applicable to FPGA verification.

<img src="https://m.media-amazon.com/images/I/51mThMxyi+L._SY445_SX342_QL70_FMwebp_.jpg" alt="Principles of Functional Verification" height="120"/>

[2] A. B. Mehta, *SystemVerilog Assertions and Functional Coverage: Guide to Language, Methodology and Applications*, 3rd ed. Cham, Switzerland: Springer, 2016.  
    * Focus: Advanced verification techniques using SystemVerilog assertions, functional coverage, and coverage-driven verification for FPGA designs.

<img src="https://m.media-amazon.com/images/I/611tMfyBvXL._SY466_.jpg" alt="SystemVerilog Assertions and Functional Coverage: Guide to Language, Methodology and Applications" height="120"/>

## 3. Kits

### 3.1 AMD Virtex™ UltraScale+™ FPGA VCU118 Evaluation Kit  [[2]](https://www.amd.com/en/products/adaptive-socs-and-fpgas/evaluation-boards/vcu118.html)
> Use Software Stack 1.2

![](img/vcu118-features.jpg)

### 3.2 Amazon EC2 F2 FPGA Instances [[5]](https://aws.amazon.com/ec2/instance-types/f2/)
> Cloud-based FPGA acceleration for high-performance computing workloads.

## 4. Tutorials  

### 4.1 Vitis Model Composer Tutorials [[4]](https://github.com/Xilinx/Vitis_Model_Composer/blob/HEAD/Tutorials/README.md)

### 4.2 AMD - Adaptable Learning [[8]](https://learningcatalog-amd.netexam.com/)


## References

[1] IBM, "What is a Field-Programmable Gate Array (FPGA)?," IBM. [Online]. Available: https://www.ibm.com/think/topics/field-programmable-gate-arrays. [Accessed: Sep. 22, 2025].  

[2] AMD, "Virtex UltraScale+ FPGA VCU118 Evaluation Kit," AMD. [Online]. Available: https://www.amd.com/en/products/adaptive-socs-and-fpgas/evaluation-boards/vcu118.html. [Accessed: Sep. 22, 2025].  

[3] AMD, "Vivado ML Edition - 2025.1," AMD. [Online]. Available: https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/2025-1.html. [Accessed: Sep. 22, 2025].

[4] Xilinx, "Vitis Model Composer Tutorials," GitHub, [Online]. Available: https://github.com/Xilinx/Vitis_Model_Composer/blob/HEAD/Tutorials/README.md. [Accessed: Nov. 30, 2025].

[5] Amazon Web Services, "Amazon EC2 F2 Instances," AWS. [Online]. Available: https://aws.amazon.com/ec2/instance-types/f2/. [Accessed: Dec. 23, 2025].

[6] AWS, "AWS FPGA Development Kit," GitHub. [Online]. Available: https://github.com/aws/aws-fpga. [Accessed: Dec. 23, 2025].

[7] Amazon Web Services, "FPGA Developer AMI," AWS Marketplace. [Online]. Available: https://aws.amazon.com/marketplace/pp/prodview-f5kjsenkfkz5u. [Accessed: Dec. 23, 2025].

[8] AMD, "Adaptable Learning," AMD. [Online]. Available: https://learningcatalog-amd.netexam.com/. [Accessed: Dec. 23, 2025].

