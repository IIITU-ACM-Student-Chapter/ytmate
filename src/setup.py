def main(env_dir="venv", req_file="requirements.txt"):
    import venv
    import os
    import sys
    import subprocess as sbp

    env_builder = venv.EnvBuilder(with_pip=True, clear=True)
    env_builder.create(env_dir=env_dir)

    if sys.platform == "win32":
        python_exe = os.path.join(env_dir, "Scripts", "python.exe")
    else:
        python_exe = os.path.join(env_dir, "bin", "python")
    
    if os.path.exists(req_file):
        print(f"Installing requirements from {req_file}...")
        sbp.check_call([python_exe, "-m", "pip", "install", "-r", req_file])
    else:
        print(f"No {req_file} found. Skipping installation.")


if __name__ == "__main__":
    main()