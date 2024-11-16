import os

def deploy():
    deployment_dir = "deployment"

    if not os.path.exists(deployment_dir):
        os.makedirs(deployment_dir)
        print(f"Created deployment directory: {deployment_dir}")
    else:
        print(f"Deployment directory already exists: {deployment_dir}")

    deployment_file = os.path.join(deployment_dir, "deployed.txt")
    with open(deployment_file, "w") as file:
        file.write("Deployment successful!\n")
        print(f"Deployment file created at: {deployment_file}")

if __name__ == "__main__":
    deploy()