import subprocess
import time

def main(source_path):
    print(source_path)
    ssh_tunnel_script = f"{source_path}open_ssh_tunnel.sh"
    print("Starting SSH tunnels...")
    print(ssh_tunnel_script)
    subprocess.run(ssh_tunnel_script, shell=True, check=True)

    # print("Starting report_email.py in background...")
    # subprocess.Popen(["python3", f"{source_path}report_email.py"])
    # time.sleep(2)
    #
    # print("Starting transfer_from_farm_pc.py in background...")
    # subprocess.Popen(["python3", f"{source_path}transfer_from_farm_pc.py"])
    # time.sleep(2)

    print("Starting hanwha_rtsp_multi.py...")
    subprocess.run(["python3", f"{source_path}hanwha_rtsp_multi.py"])

if __name__ == '__main__':
    main("/home/fo18103/PycharmProjects/WhyndhurstVideoTransfer/")

