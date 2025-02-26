import yaml
import os
import random
from datetime import datetime

# Define the default settings, ensuring all original settings are included
CONFIG = {
    # General Options
    "logic_filename": "router_logic.txt",
    "nodes_filename": "router_nodes.txt",
    "retry_limit": 750,
    "retry_limit_close": 1000,
    "time_limit": random.randint(600, 1500),
    "fg_cache_limit": 10000,
    "map_size": round(random.uniform(0, 1), 2),
    "map_strictness": round(random.uniform(0, 1), 2),
    "avoid_softlocks": True,
    "skip_complex_nodes": round(random.uniform(0, 1), 2),
    "lazy_complex_nodes": False,
    "goal_based_missables": random.choice([True, False]),
    "no_logic": False,
    
    # MN64 Specific Options
    "fix_bad_maps": random.choice([True, False]),
    "fixed_singletons": round(random.uniform(0, 1), 2),
    "cluster_bgm": random.choice([True, False]),
    "completionist": random.choice([True, False]),
    "all_warps": random.choice([True, False]),
    "randomize_keys": random.randint(0, 3),
    "randomize_pickups": random.choice([True, False]),
    "randomize_enemies": random.choice([True, False]),
    "enable_debug": True,
    "start_camera": random.choice([True, False]),
    "start_minimaru": random.choice([True, False]),
    "start_flute": random.choice([True, False]),
    "start_mermaid": random.choice([True, False]),
    "flute_anywhere": True,
    "start_snow": random.choice([True, False]),
    "ice_kunai_logic": random.choice([True, False]),
    "ryo_hover_logic": random.choice([True, False]),
    "jp_super_jump_logic": random.choice([True, False]),
    "sasuke_mode": random.choice([True, False]),
    "hard_mode": random.choice([True, False]),
    "automash": random.choice([True, False]),
}

def main():
    # Ensure the "Random Seeds" directory exists
    output_dir = "Random Seeds"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate output file name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"randomized_{timestamp}.yaml")
    
    # Save the modified YAML file with ordered keys
    with open(output_file, "w") as file:
        yaml.dump(CONFIG, file, default_flow_style=False, sort_keys=False)
    
    print(f"Randomized YAML saved to: {output_file}")

if __name__ == "__main__":
    main()
