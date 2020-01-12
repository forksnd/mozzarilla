# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

This project also inherits changes from [Binilla](https://github.com/MosesofEgypt/binilla).

## [1.7.0] Into the GPLv3
Something that is very important to us is collaboration and the ability to share knowledge. Since this library is just to help mod some games, we've decided that switching to GPLv3 is the right thing to do for us to avoid any future loss of knowledge.

### Added
 - Button that opens config directory.
 - Button that resets the custom style to either a default light or dark theme.
 - Michelle to the authors!
 - Sound compilation tool. (You can compile Xbox Adpcm and PCM from wave files now!)
 - This changelog!

### Changed
 - Config is now saved in current_working_directory/mek_config on Windows. And ~/.local/share/mek/ on Linux.
 - Dependency filepath validation is now updated every time you type something.
 - Dependency filepaths are searched for case insensitively independent of operating system filesystem case sensitivity.
 - Fix symlinks not working.
 - Improve some error strings.
 - Make numerous path handling changes to support POSIX systems.
 - Shorten tags_dir string if inside of current user's home.
 - Use correct units in directory_frame.
 - Use kdialog whenever available instead of default tkinter filepicker.
 - Use more commonly available fonts as defaults on Linux.
 - Use pathlib Path objects where applicable to ease compatibility with multiple operating systems.
 - **THIS PROJECT IS NOW LICENSED UNDER THE GNU General Public License version 3**

### Removed
 - **REMOVED SUPPORT FOR VERSIONS OF PYTHON BELOW 3.5**