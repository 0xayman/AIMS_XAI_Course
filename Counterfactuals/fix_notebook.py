import json

path = "/home/aymantarig/Downloads/AIMS/AIMS_XAI_Inga/Counterfactuals/Counterfactuals_multiobj.ipynb"

with open(path, "r") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source = "".join(cell["source"])
        
        # Fix boundary types
        if "('Gender', 'todo')" in source:
            source = source.replace("('Gender', 'todo')", "('Gender', 'fixed')")
            source = source.replace("('Married', 'todo')", "('Married', 'unique')")
            source = source.replace("('Dependents', 'todo')", "('Dependents', 'fixed')")
            source = source.replace("('Education', 'todo')", "('Education', 'increase')")
            source = source.replace("('Self_Employed', 'todo')", "('Self_Employed', 'unique')")
            source = source.replace("('ApplicantIncome', 'todo')", "('ApplicantIncome', 'range')")
            source = source.replace("('CoapplicantIncome', 'todo')", "('CoapplicantIncome', 'range')")
            source = source.replace("('LoanAmount', 'todo')", "('LoanAmount', 'fixed')")
            source = source.replace("('Loan_Amount_Term', 'todo')", "('Loan_Amount_Term', 'unique')")
            source = source.replace("('Credit_History', 'todo')", "('Credit_History', 'unique')")
            source = source.replace("('Property_Area', 'todo')", "('Property_Area', 'unique')")
            
        # Fix X_train undefined
        if "numerical_features = [x for x in X_train.columns" in source:
            source = source.replace("X_train.columns", "x.columns")
            
        # Fix tuple unpacking
        if "counterfactuals, study = get_counterfactuals(" in source:
            source = source.replace("counterfactuals, study =", "counterfactuals =")

        # Fix feature info in In[17] if any
        if "generate_individual(X_train,x,feat_conf[\"feature_info\"])" in source:
             # Actually, if X_train is not defined yet, wait, In[17] defined X_train.
             pass
             
        # Rewrite source list while preserving newlines properly
        lines = source.split("\n")
        new_source = []
        for i, line in enumerate(lines):
            if i < len(lines) - 1:
                new_source.append(line + "\n")
            else:
                if line:
                    new_source.append(line)
        cell["source"] = new_source
        
        # Clear output and execution count
        if "outputs" in cell:
            cell["outputs"] = []
        if "execution_count" in cell:
            cell["execution_count"] = None

with open(path, "w") as f:
    json.dump(nb, f, indent=1)

print("Notebook modified successfully.")
