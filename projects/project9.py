class Robot:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        print(f"Hello! I am {self.name}.")
        print(f"Model: {self.model}")
        print(f"My purpose is to {self.purpose}.")
        print("It is nice to meet you, human!")


# Create a robot and have it introduce itself
robot = Robot(
    name="ARIA",
    model="AR-7000",
    purpose="assist humans with everyday tasks"
)

robot.introduce()