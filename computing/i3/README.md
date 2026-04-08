# i3

## [My i3 custom config and i3status](https://github.com/augustodamasceno/dotfiles/i3)  

## i3 Window Manager Cheat Sheet by Gemini 3.1 Pro

*Note: `$mod` refers to the modifier key. By default, this is usually the `Alt` key (Mod1) or the `Super/Windows` key (Mod4).*

## 1. Session & System Management

| Action | Keybinding | Command/Description |
| :--- | :--- | :--- |
| **Reload Config** | `$mod + Shift + c` | Reloads `~/.config/i3/config` (useful after edits). |
| **Restart i3** | `$mod + Shift + r` | Restarts i3 in place (preserves layout/open apps). |
| **Exit/Log Out** | `$mod + Shift + e` | Prompts to exit the i3 session. |

## 2. Launching Applications

| Action | Keybinding | Command/Description |
| :--- | :--- | :--- |
| **Open Terminal** | `$mod + Enter` | Opens default terminal. |
| **App Launcher** | `$mod + d` | Opens `dmenu` or `rofi` to run a command/app. |
| **Kill Window** | `$mod + Shift + q` | Closes the currently focused window. |

## 3. Window Focus & Navigation

*i3 uses the home row `j k l ;` by default, but arrow keys also work.*

| Action | Keybinding |
| :--- | :--- |
| **Focus Left** | `$mod + j` or `$mod + Left Arrow` |
| **Focus Down** | `$mod + k` or `$mod + Down Arrow` |
| **Focus Up** | `$mod + l` or `$mod + Up Arrow` |
| **Focus Right** | `$mod + ;` or `$mod + Right Arrow` |
| **Toggle Focus (Floating)**| `$mod + Space` (Switches focus between floating and tiled windows) |
| **Focus Parent** | `$mod + a` (Selects the parent container of the current window) |

## 4. Moving Windows

| Action | Keybinding |
| :--- | :--- |
| **Move Left** | `$mod + Shift + j` or `$mod + Shift + Left Arrow` |
| **Move Down** | `$mod + Shift + k` or `$mod + Shift + Down Arrow` |
| **Move Up** | `$mod + Shift + l` or `$mod + Shift + Up Arrow` |
| **Move Right** | `$mod + Shift + ;` or `$mod + Shift + Right Arrow` |

## 5. Splits & Layouts

| Action | Keybinding | Description |
| :--- | :--- | :--- |
| **Split Horizontal** | `$mod + h` | Next newly opened window will split side-by-side. |
| **Split Vertical** | `$mod + v` | Next newly opened window will split top-and-bottom. |
| **Fullscreen** | `$mod + f` | Toggles the focused window to full screen. |
| **Toggle Floating** | `$mod + Shift + Space` | Detaches the window from the tiling grid. |
| **Stacking Layout** | `$mod + s` | Windows stack vertically (only title bars visible). |
| **Tabbed Layout** | `$mod + w` | Windows stack horizontally (like browser tabs). |
| **Split/Default Layout**| `$mod + e` | Returns to standard tiling. |

## 6. Workspaces

| Action | Keybinding |
| :--- | :--- |
| **Switch Workspace** | `$mod + [0-9]` (e.g., `$mod + 1`, `$mod + 2`) |
| **Move Window to Workspace**| `$mod + Shift + [0-9]` |

## 7. The Scratchpad

*The scratchpad is a hidden workspace. It is useful for background apps that you want to call up quickly without taking up permanent screen space.*

| Action | Keybinding | Description |
| :--- | :--- | :--- |
| **Move to Scratchpad** | `$mod + Shift + minus` | Sends focused window to the hidden scratchpad. |
| **Show Scratchpad** | `$mod + minus` | Cycles through windows currently in the scratchpad. |

## 8. Resizing Windows

*Resizing in i3 requires entering a specific "Resize Mode".*

1. **Enter Resize Mode:** Press `$mod + r`.
2. **Adjust Size:** Use `j k l ;` or `Arrow Keys` to expand or shrink the window.
3. **Exit Resize Mode:** Press `Escape` or `Enter`.

---

## Configuration File Basics (`~/.config/i3/config`)

### Setting the Modifier Key

    # Use Alt key
    set $mod Mod1

    # Use Super/Windows key
    set $mod Mod4

### Autostarting Applications

* **`exec`**: Runs the command once when i3 starts.
* **`exec_always`**: Runs the command every time i3 starts or is reloaded (`$mod + Shift + c`).

    # Start a compositor (for transparency/shadows)
    exec --no-startup-id picom -b

    # Restore wallpaper
    exec_always --no-startup-id feh --bg-scale ~/Pictures/wallpaper.jpg

### Custom Keybindings (`bindsym`)

    # Syntax: bindsym [key combo] [command]
    bindsym $mod+Shift+f exec alacritty -e yazi
    bindsym $mod+Shift+b exec firefox

### Window Rules (`for_window`)

Force specific applications to open in floating mode or on specific workspaces. Use `xprop | grep WM_CLASS` in the terminal to find the class name.

    # Make calculators float
    for_window [class="Qalculate-gtk"] floating enable

    # Always open VS Code on workspace 2
    assign [class="Code"] 2
