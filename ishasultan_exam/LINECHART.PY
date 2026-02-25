import matplotlib.pyplot as plt

def get_data_from_user():
    print("=== Chart Builder ===")
    
    title = input("Enter chart title: ")
    x_label = input("Enter X-axis label: ")
    y_label = input("Enter Y-axis label: ")
    
    print("\nEnter your data points (type 'done' when finished):")
    x_data = []
    y_data = []
    
    while True:
        x_val = input(f"  X value #{len(x_data)+1} (or 'done'): ")
        if x_val.lower() == 'done':
            if len(x_data) < 2:
                print("  Please enter at least 2 data points.")
                continue
            break
        try:
            y_val = float(input(f"  Y value for '{x_val}': "))
            x_data.append(x_val)
            y_data.append(y_val)
        except ValueError:
            print("  ⚠️  Y value must be a number. Try again.")
    
    return x_data, y_data, title, x_label, y_label

def plot_chart(x_data, y_data, title, x_label, y_label):
    plt.figure(figsize=(8, 5))
    plt.plot(x_data, y_data, marker='o', linestyle='-', color='steelblue', linewidth=2)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    x_data, y_data, title, x_label, y_label = get_data_from_user()
    plot_chart(x_data, y_data, title, x_label, y_label)
