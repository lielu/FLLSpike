# Repository for WeLostAPiece FLL robotics team

## Getting Started
Follow the instructions below to get started on Python and Spike programming for FLL robot games.

1. Install `Python 3.12` from [python.org](https://www.python.org/downloads/). For Windows, make sure to select `Add Python to PATH` during installation. You will also need to install [`pip`](https://pip.pypa.io/en/stable/installation/) using the following commands on Windows:
```sh
    py -m ensurepip --upgrade
```
2. (Optional) Install Spike from https://education.lego.com/en-us/downloads/spike-app/software/ if you are not running the web version (https://spike.legoeducation.com).
3. Download [git](https://git-scm.com/downloads), [Github Desktop](https://desktop.github.com/), and [Github CLI](https://cli.github.com/). Note: for Github CLI, you will need administrator access to install it (on Windows); if you don't have it, you can download the [zip file with name "GitHub CLI <version> windows amd64"](https://github.com/cli/cli/releases) and execute the `gh` command directly from the extracted folder.
4. Follow instructions at https://docs.github.com/en/get-started/quickstart/set-up-git to set up git and link it with Github Desktop and Github CLI. The recommended way is to use Github CLI `gh auth login` to login with your Github account.
5. Clone this repository to your local machine using Terminal (macOS/Linux) or Command Prompt (Windows):
```sh
    cd <your-local-repo-folder>
    git clone https://github.com/lielu/FLLSpike.git
```

## LLSP3 and Python Files
When you create a Spike project, the code (Python or block code) will be saved as LLSP3 files. LLSP3 files are the original format used by the Spike app or website. When you create a new project, choose the `Python` option, and save it to the `FLLSpike/src/runs` folder with a chosen project name using the `Save As` menu. This will allow the LLSP3 files to be saved to Github backend store later.

### Saving LLSP3 and Python files into Github
Python code is not directly saved in the LLSP3 files. Rather, it's captured in another format, which we need to extract it from the LLSP3 files. To extract the Python code from LLSP3 files and generate library code that can be installed at runtime automatically, use the `utils/monitor_llsp3_to_python_mac.py` or `utils/monitor_llsp3_to_python_win.py` script with the following command:

#### macOS
Run the following command to start the LLSP3 file monitoring process as a background service:
```sh
    cd <your-local-repo-folder>/FLLSpike/utils
    python3 monitor_llsp3_to_python_mac.py start --directory <your-local-repo-folder>/FLLSpike/src/libs
```
If you want to stop the LLSP3 file monitoring process, run the following command:
```sh
    cd <your-local-repo-folder>/FLLSpike/utils
    python3 monitor_llsp3_to_python_mac.py stop
```
#### Windows
Run the following command to start the LLSP3 file monitoring process as a Windows service:
```sh
    cd <your-local-repo-folder>/FLLSpike/utils
    monitor_llsp3_windows.bat
```
If you want to stop the LLSP3 file monitoring service, run the following command:
```sh
    cd <your-local-repo-folder>/FLLSpike/utils
    python monitor_llsp3_to_python_windows.py stop
```
Please note that the extracted Python code shouldn't be edited directly outside of Spike app. The primary purpose of the extracted Python code is to allow others to review the code changes before they are pushed to Github, and also check the Python code changes later.

### Loading LLSP3 files into Spike
In Spike app, go to `File -> Open`, and select the `LLSP3` file in the `src` folder, or any other folder containing LLSP3 files.

### Pushing LLSP3 file changes to Github
After you make changes to the Spike projects, which will update the LLSP3 files and the extracted Python code, you can push the changes to Github by running the following command:
```sh
    cd <your-local-repo-folder>/FLLSpike
    git add .
    git commit -m "<your description of the changes, e.g. improve Straight function>"
    git push
```

## Folder Structure
### `src`: Contains the main code for the robot game
#### `src/runs`: Contains the LLSP3 files for the main code for the robot game
We will either have each run in code such as `run0.llsp3`, `run1.llsp3`, etc., or have one main code to capture all runs.
#### `src/libs`: Contains the LLSP3 files for the library code that can be used across multiple runs.
The libraries include code for the robot such as `Straight`, `Turn`, `Arm`, `Claw`, `Sensor`, `Display`, etc. The [library document](src/libs/LIBRARY.md) provides more details.
### `docs`: Contains the documentation for robot game, innovation project, and more

### `utils`: Contains the utility scripts for FLL robotics logistics

