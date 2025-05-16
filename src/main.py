import wandb
from tqdm import tqdm

from config import get_args
from dataset import *


def main(args):

    # TODO: Make dataset & Dataloader
    dataset = MyDataset(**vars(args))
    t_loader = DataLoader()
    
    # TODO: Load model
    model = None
    # TODO: Load optimizer & scheduler
    optimizer = None
    scheduler = None
    
    if args.wandb:
        print(f"\nLogging with Weight & Biases...\n")
        wandb.init(project= "", # project name
                   name= "", # Each exp logging name
                   dir= "") # where to save wandb log
        wandb.watch(model)
    
    """Training phase"""        
    
    
    print(f"\nTraining is Done.\n")
    
    return 



if __name__ == "__main__":
    args = get_args()