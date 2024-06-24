#!/usr/bin/python3
#### Modules #####
import sys
import time
import subprocess
import os

##### Variables #####
current_dir = os.getcwd()
kvm_dir = f"/home/{os.getlogin()}/Documents/KVM"
config_file = f"{current_dir}/kvm-manager.conf"
delay = 5


#### Functions ####
def confirm_request(request):
    confirm = input("Please confirm your **" + request + "** request (yes) : ")
    if confirm != "yes":
        print("You didn't confirm with 'yes'. Bye Bye!")
        sys.exit(44)


def open_file(file_path, mode):
    try:
        file = open(file_path, mode)
    except FileNotFoundError:
        print(f"File {file_path} does not exist", end="\n\n")
        file = None
    except PermissionError:
        print(f"You don't have permission to access {file_path}", end="\n\n")
        file = None
    finally:
        return file  # 'file' is an object or None


def clone_vm(distro, vm, lan, kvm_dir):
    template = "0-" + distro
    clone_cmd = [
        "virt-clone",
        "--original",
        template,
        "--name",
        vm,
        "--file",
        f"{kvm_dir}/{vm}.qcow2",
    ]
    subprocess.run(clone_cmd)
    time.sleep(delay)
    detach_cmd = ["virsh", "detach-interface " + vm + " network --persistent"]
    subprocess.run(detach_cmd)
    time.sleep(delay)
    attach_cmd = [
        "virsh",
        "attach-interface " + vm + " network " + lan + " --model virtio --persistent",
    ]
    subprocess.run(attach_cmd)
    time.sleep(delay)
    start_vm(vm)


def start_vm(vm):
    start_cmd = ["virsh", "start " + vm]
    subprocess.run(start_cmd)


def shutdown_vm(vm):
    shutdown_cmd = ["virsh", "shutdown " + vm]
    subprocess.run(shutdown_cmd)


def destroy_vm(vm):
    shutdown_vm(vm)
    delay = 5
    time.sleep(delay)
    undefine_cmd = ["virsh", "undefine --remove-all-storage " + vm]
    subprocess.run(undefine_cmd)


def list_vm():
    list_cmd = ["virsh", "list --state-running"]
    subprocess.run(list_cmd)


def trigger_request(request, line, kvm_dir):
    line = line.strip()
    line = line.split("|")
    vm = line[0]
    distro = line[1]
    lan = line[2]
    user = line[3]
    port = line[4]

    match request:
        case "clone":
            clone_vm(distro, vm, lan, kvm_dir)
        case "start":
            start_vm(vm)
        case "shutdown":
            shutdown_vm(vm)
        case "destroy":
            destroy_vm(vm)
        case "status":
            list_vm()


##### Main code ####
try:
    request = sys.argv[1]
except:
    print("**** Usage: clone|start|shutdown|status|destroy ****")
    sys.exit(22)

match request:
    case "clone" | "destroy":
        confirm_request(request)
        print(f"Triggering your **{request}** request ...")
    case "start" | "shutdown" | "status":
        print(f"Triggering your **{request}** request ...")
    case _:
        print("**** Usage: clone|start|shutdown|destroy ****")
        sys.exit(33)

config = open_file(config_file, "r")
if config:
    try:
        for line in config:
            if (line == "\n") or (line.startswith("#")):  # TODO add regex for #
                continue
            trigger_request(request, line, kvm_dir)
    except:
        print(f"Error while reading the file {config}", end="\n\n")
    finally:
        config.close()
