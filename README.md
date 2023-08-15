# Debug Mode Toggling

Enhance your Sublime Text debugging experience with these toggleable debug logging options:

- **Command Logging**: Toggle the logging of commands to the console when executed.
- **Input Logging**: Toggle the logging of all key presses to the console. Useful for identifying specific keyboard key names.
- **Result Regex Logging**: Toggle the logging of result regexes. Useful for debugging `"file_regex"` and `"line_regex"` in build systems.
- **Index Printing**: Toggle the printing of indexing logs to the console.
- **Build System Logging**: Toggle the printing of build system logs to the console.
- **Control Tree Logging**: Toggle the logging of control tree information. When enabled, pressing `ctrl+alt` and clicking will log the control tree under the mouse to the console.
- **FPS Logging**: Toggle the logging of rendering timings, such as frames per second.

For more comprehensive information, refer to [Sublime Text's API Documentation](https://www.sublimetext.com/docs/api_reference.html).

## Installation

**Method 1: Using Package Control**

1. Open Sublime Text.
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS) to open the Command Palette.
3. Type "Package Control: Install Package" and press `Enter`.
4. In the input field, type "ToggleDebugMode" and select it from the list of available packages.

**Method 2: Manual Installation**

1. Visit the [ToggleDebugMode GitHub repository](https://github.com/gerardroche/sublime-toggle-debug-mode).
2. Click on the "Code" button and select "Download ZIP."
3. Extract the downloaded ZIP file.
4. Open Sublime Text and go to `Preferences -> Browse Packages...` to open the Packages folder.
5. Copy the "ToggleDebugMode" folder from the extracted ZIP and paste it into the Packages folder.

**Method 3: Manual Git Repository Installation**

1. Open a terminal or command prompt.
2. Navigate to the Sublime Text Packages directory:
    - On Windows: `%APPDATA%\Sublime Text\Packages`
    - On macOS: `~/Library/Application Support/Sublime Text/Packages`
    - On Linux: `~/.config/sublime-text/Packages`
3. Clone the plugin repository directly into the Packages directory using Git:
   ```
   git clone https://github.com/gerardroche/sublime-toggle-debug-mode.git ToggleDebugMode
   ```

## Commands

Fine-tune your debugging experience with these powerful commands:

| Command                                            | Description                                       |
| :------------------------------------------------- | :------------------------------------------------ |
| **ToggleDebugMode: Logging - Disable all**         | Disable all logging                               |
| **ToggleDebugMode: Logging - Enable all**          | Enable all logging                                |
| **ToggleDebugMode: Logging - Toggle Build System** | Toggle build system logging                       |
| **ToggleDebugMode: Logging - Toggle Command**      | Toggle command logging                            |
| **ToggleDebugMode: Logging - Toggle Control Tree** | Toggle control tree logging                       |
| **ToggleDebugMode: Logging - Toggle Fps**          | Toggle FPS logging                                |
| **ToggleDebugMode: Logging - Toggle Index**        | Toggle index logging                              |
| **ToggleDebugMode: Logging - Toggle Input**        | Toggle input logging                              |
| **ToggleDebugMode: Logging - Toggle Result Regex** | Toggle result regex logging                       |

Experience enhanced debugging functionalities. Try out these commands to streamline your debugging process.

## License

Released under the [GPL-3.0-or-later License](LICENSE).
