# Sublime Debug Logging

Boost your Sublime Text debugging with this plugin. Adds commands to enable or disable editor logging features from the Command Palette.

## Features

- **Command Logging**: Logs executed commands to the console.
- **Input Logging**: Captures all key presses—perfect for identifying key names.
- **FPS Logging**: Tracks rendering timings, like frames per second.
- **Result Regex Logging**: Debugs `"file_regex"` and `"line_regex"` in build systems.
- **Indexing Logging**: Prints indexing logs to the console.
- **Build System Logging**: Monitors build system activity.
- **Control Tree Logging**: Logs the control tree under the mouse when clicking with `Ctrl+Alt` (Windows/Linux) or `Cmd+Alt` (macOS).

For detailed API info, see the [Sublime Text API Documentation](https://www.sublimetext.com/docs/api_reference.html).

## Installation

Choose your preferred method to install the `ToggleDebugMode` plugin:

### Option 1: Package Control
1. Open Sublime Text and press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS).
2. Type `Package Control: Install Package` and hit `Enter`.
3. Search for `ToggleDebugMode` and select it to install.

### Option 2: Git Clone
1. Open a terminal and navigate to your Sublime Text Packages folder:
   - Windows: `%APPDATA%\Sublime Text\Packages`
   - macOS: `~/Library/Application Support/Sublime Text/Packages`
   - Linux: `~/.config/sublime-text/Packages`
2. Run:
   ```
   git clone https://github.com/gerardroche/sublime-toggle-debug-mode.git ToggleDebugMode
   ```

## Available Commands

Access these commands via the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) to customize your debugging:

| Command                            | Description                          |
|------------------------------------|--------------------------------------|
| `ToggleDebugMode: Enable Logging`  | Activates all logging features       |
| `ToggleDebugMode: Disable Logging` | Deactivates all logging features     |
| `ToggleDebugMode: Toggle Command Logging`       | Toggles command logging       |
| `ToggleDebugMode: Toggle Input Logging`         | Toggles key press logging     |
| `ToggleDebugMode: Toggle FPS Logging`           | Toggles FPS logging           |
| `ToggleDebugMode: Toggle Result Regex Logging`  | Toggles regex logging         |
| `ToggleDebugMode: Toggle Index Logging`         | Toggles indexing logging      |
| `ToggleDebugMode: Toggle Build System Logging`  | Toggles build system logging  |
| `ToggleDebugMode: Toggle Control Tree Logging`  | Toggles control tree logging  |

## Usage Tips
- Use `Input Logging` to troubleshoot key bindings.
- Enable `Result Regex Logging` to refine build system regex patterns.
- Activate `Control Tree Logging` and click with `Ctrl+Alt`/`Cmd+Alt` to inspect UI elements.

## License

This plugin is released under the [GPL-3.0-or-later License](LICENSE).

---

Happy debugging!
