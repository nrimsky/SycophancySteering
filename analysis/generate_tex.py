def process_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    # Dictionary to store data for each model
    model_data = {}

    # Process each line
    for line in data:
        model, x, y = line.split()
        if model not in model_data:
            model_data[model] = []
        model_data[model].append((float(x), float(y)))

    # Generate LaTeX code for each layer
    with open("tex_"+file_path, 'w') as file:
        for model in model_data:
            coordinates = " ".join(f"({x}, {y})" for x, y in model_data[model])
            file.write(f"\\addplot coordinates {{\n{coordinates}\n}};\n\\addlegendentry{{Layer {model}}}\n")

process_data('max_new_tokens=100_type=in_distribution_few_shot=none_do_projection=False_use_base_model=False_model_size=7b_add_every_token_position=False.txt')
