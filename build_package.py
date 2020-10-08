import os
import string
import shutil
import argparse
import tarfile

version = "0.0"
dist_path = "dist"

def package_dir():
    return f"weewx-json_{version}"


def clean_dist():
    if os.path.exists(dist_path):
        shutil.rmtree(dist_path)

    os.mkdir(dist_path)

def copy_skin():
    shutil.copytree("skins", os.path.join(dist_path, package_dir(), "skins"))


def build_changelog():
    shutil.copy("CHANGELOG.md", 
                os.path.join(dist_path, package_dir(), "changelog"))


def build_readme():
    shutil.copy2("README.md",
                 os.path.join(dist_path, package_dir(), "readme.txt"))


def copy_license():
    shutil.copy2("LICENSE",
                 os.path.join(dist_path, package_dir(), "LICENSE"))


def file_paths():
    original_dir = os.getcwd()
    os.chdir(os.path.join(dist_path, package_dir()))

    paths = []
    for root, _, files in os.walk("skins/JSON"):
        for filename in files:
            paths.append(os.path.join(root, filename))

    os.chdir(original_dir)

    return ("skins/JSON", paths)


def install_file():
    output_string = ""
    with open("dist-template/install.py.template", "r") as input_file:
        tp = string.Template(input_file.read())
        output_string = tp.substitute({
            "version": version,
            "file_paths": file_paths().__repr__()
            })

    output_path = os.path.join(dist_path, package_dir(), "install.py")
    with open(output_path, "w") as output_file:
        output_file.write(output_string)


def create_zip():
    archive_path = os.path.join(dist_path, package_dir() + ".tar.gz")
    with tarfile.open(archive_path, "w:gz") as archive:
        archive.add(
            os.path.join(dist_path, package_dir()), arcname=package_dir())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Package the JSON extension')
    parser.add_argument('--set-version', default="0.0",
                        help='Version number to build')

    args = parser.parse_args()
    version = args.set_version

    clean_dist()

    copy_skin()
    build_changelog()
    build_readme()
    copy_license()
    install_file()

    create_zip()
