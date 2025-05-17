import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Train HMD Model",  allow_abbrev=False)
    
    """Virtual machine settings"""
    parser.add_argument("--gpu_num", type=str, default= '0',
                        help= "gpu index to use 1 gpu")
    parser.add_argument("--debug", action="store_true",
                        help="activating debugging mode",)
    parser.add_argument("--wandb", action="store_true",
                        help="use Weight and Biases tool", )
    
    """Path"""
    parser.add_argument("--train_datapath", type=str, default= None)
    parser.add_argument("--test_datapath", type=str, default= None)
    parser.add_argument("--save_path", type=str, default= None, 
                        help= "where to save your exp result & model checkpoint")
    
    """Data preprocessing"""
    parser.add_argument("--num_workers", type=int, default= 8)
    
    """Data augmentation"""
    parser.add_argument("--mixup", action="store_true",
                        help= "If True, use mix-up data augmentation")
    
    """Hyper-parameters settings"""
    parser.add_argument("--seed", type=int, default= 42)
    parser.add_argument("--total_epochs", type=int, default= 100)
    parser.add_argument("--train_bs", type=int, default= None, help= "train batch size")
    parser.add_argument("--val_bs", type=int, default= None, help= "val batch size")
    
    # Optimizer
    parser.add_argument("--learning_rate", type= float, default= 1e-5)
    parser.add_argument("--weight_decay", type= float, default= 1e-5)
    parser.add_argument("--betas", type= tuple, default= (0.9, 0.999))
    
    parser.add_argument("--patience", type=int, default=None, 
                        help= "early-stopping counter")
    
    # args = parser.parse_args() >> Cannot get args in .ipynb files...!
    args, _ = parser.parse_known_args()
    
    if args.debug: # If debugging mode, do not use Weight & Biases packages.
        args.wandb= False
        
    return args
    
if __name__ == "__main__":
    args = get_args()
    print(args)