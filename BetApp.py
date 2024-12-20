from shiny import App, ui, render
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# UI 
app_ui = ui.page_fluid(
    ui.h2("DNA Methylation Beta Value Density Plot"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_file("file_input", "Upload Beta Value File (.txt)", accept=[".txt"]),
            ui.input_checkbox("remove_na", "Remove NA Values", value=True),
            ui.input_action_button("plot_btn", "Generate Plot")
        ),
        ui.output_plot("beta_plot"),
        ui.output_text_verbatim("data_preview")
    )
)

# Server
def server(input, output, session):
    @output
    @render.plot
    def beta_plot():
        file_info = input.file_input()
        if file_info is None:
            return
        
        # Read file
        file_contents = file_info[0]["datapath"]
        df = pd.read_csv(file_contents, sep="\t", header=None, names=["CpG_Site", "Beta_Value"])
        
        if input.remove_na():
            df = df.dropna()
        um_df = df[df["Beta_Value"] <= 0.2]  # Hypomethylated
        hm_df = df[(df["Beta_Value"] > 0.2) & (df["Beta_Value"] < 0.8)]  # Hemimethylated
        m_df = df[df["Beta_Value"] >= 0.8]  # Hypermethylated
        
        plt.figure(figsize=(10, 6))
        sns.kdeplot(um_df["Beta_Value"], color="green", label="Hypomethylated (UM)", fill=True, alpha=0.5)
        sns.kdeplot(hm_df["Beta_Value"], color="blue", label="Hemimethylated (HM)", fill=True, alpha=0.5)
        sns.kdeplot(m_df["Beta_Value"], color="purple", label="Hypermethylated (M)", fill=True, alpha=0.5)
        
        plt.xlabel("Beta Values")
        plt.ylabel("Density")
        plt.title("DNA Methylation Levels - Density Plot")
        plt.legend(loc="upper right")
        plt.tight_layout()
        plt.show()

    @output
    @render.text
    def data_preview():
        file_info = input.file_input()
        if file_info is None:
            return "No file uploaded."
        
        file_contents = file_info[0]["datapath"]
        df = pd.read_csv(file_contents, sep="\t", header=None, names=["CpG_Site", "Beta_Value"])
        return df.head().to_string(index=False)

# Run the Shinyapp
app = App(app_ui, server)
from shiny import App, ui, render
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# UI Design
app_ui = ui.page_fluid(
    ui.h2("DNA Methylation Beta Value Density Plot"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_file("file_input", "Upload Beta Value File (.txt)", accept=[".txt"]),
            ui.input_checkbox("remove_na", "Remove NA Values", value=True),
            ui.input_action_button("plot_btn", "Generate Plot")
        ),
        ui.output_plot("beta_plot"),
        ui.output_text_verbatim("data_preview")
    )
)

# Server
def server(input, output, session):
    @output
    @render.plot
    def beta_plot():
        file_info = input.file_input()
        if file_info is None:
            return
        
        # Read file
        file_contents = file_info[0]["datapath"]
        df = pd.read_csv(file_contents, sep="\t", header=None, names=["CpG_Site", "Beta_Value"])
        
        if input.remove_na():
            df = df.dropna()
        
        um_df = df[df["Beta_Value"] <= 0.2]  # Hypomethylated
        hm_df = df[(df["Beta_Value"] > 0.2) & (df["Beta_Value"] < 0.8)]  # Hemimethylated
        m_df = df[df["Beta_Value"] >= 0.8]  # Hypermethylated
        

        plt.figure(figsize=(10, 6))
        sns.kdeplot(um_df["Beta_Value"], color="green", label="Hypomethylated (UM)", fill=True, alpha=0.5)
        sns.kdeplot(hm_df["Beta_Value"], color="blue", label="Hemimethylated (HM)", fill=True, alpha=0.5)
        sns.kdeplot(m_df["Beta_Value"], color="purple", label="Hypermethylated (M)", fill=True, alpha=0.5)
        
        plt.xlabel("Beta Values")
        plt.ylabel("Density")
        plt.title("DNA Methylation Levels - Density Plot")
        plt.legend(loc="upper right")
        plt.tight_layout()
        plt.show()

    @output
    @render.text
    def data_preview():
        file_info = input.file_input()
        if file_info is None:
            return "No file uploaded."
        
        file_contents = file_info[0]["datapath"]
        df = pd.read_csv(file_contents, sep="\t", header=None, names=["CpG_Site", "Beta_Value"])
        return df.head().to_string(index=False)

# Start the app
app = App(app_ui, server)

