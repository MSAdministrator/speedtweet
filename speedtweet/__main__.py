import fire

from .speedtweet import Speed

def main(args=None):
    speed = Speed()
    fire.Fire(speed)

if __name__ == "__main__":
    main()