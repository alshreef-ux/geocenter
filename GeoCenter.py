import os
import subprocess
import ctypes
import sys

class GeoCenter:
    def __init__(self):
        self.startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    def list_startup_programs(self):
        """Lists programs in the startup folder."""
        print("Programs in Startup Folder:")
        for item in os.listdir(self.startup_folder):
            print(f"- {item}")

    def disable_startup_program(self, program_name):
        """Disables a program from the startup list."""
        try:
            program_path = os.path.join(self.startup_folder, program_name)
            if os.path.exists(program_path):
                os.remove(program_path)
                print(f"Disabled startup program: {program_name}")
            else:
                print(f"Program '{program_name}' not found in startup folder.")
        except Exception as e:
            print(f"Error disabling program: {e}")

    def optimize_boot(self):
        """Runs system commands to optimize the Windows boot process."""
        try:
            print("Optimizing boot process...")
            subprocess.run(['powercfg', '/hibernate', 'off'], check=True)
            subprocess.run(['bcdedit', '/set', '{current}', 'bootstatuspolicy', 'ignoreallfailures'], check=True)
            print("Boot optimization complete.")
        except subprocess.CalledProcessError as e:
            print(f"Error during boot optimization: {e}")

    def clear_temp_files(self):
        """Clears temporary files to reduce clutter."""
        temp_path = os.getenv('TEMP')
        try:
            print("Clearing temporary files...")
            for filename in os.listdir(temp_path):
                file_path = os.path.join(temp_path, filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
            print("Temporary files cleared.")
        except Exception as e:
            print(f"Error clearing temporary files: {e}")

    def run_as_admin(self):
        """Re-run the program with administrative privileges."""
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("Attempting to restart with administrative privileges...")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

if __name__ == "__main__":
    geo_center = GeoCenter()
    geo_center.run_as_admin()
    geo_center.list_startup_programs()
    geo_center.optimize_boot()
    geo_center.clear_temp_files()