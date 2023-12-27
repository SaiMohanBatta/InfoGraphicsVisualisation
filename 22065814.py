import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec


# function to add borders to plots
def formatplot(ax, color):
    """
    Formats the appearance of a matplotlib plot by customizing borders and ticks.

    Parameters:
    - ax (matplotlib.axes.Axes): The axes object to be formatted.
    - color (str): The color for the plot borders and ticks.

    Returns:
    None
    
    """
    # Add border
    for spine in ax.spines.values():
        spine.set_edgecolor(color)
        spine.set_linewidth(2)
    
    # Set ticks inside
    ax.tick_params(direction='in', length=6, width=2)


# Reading data from CSV files
df_accesstoElec = pd.read_csv('AccesstoElec.csv')
df_birds = pd.read_csv('Birds.csv')
df_co2 = pd.read_csv('Co2.csv')
df_renew = pd.read_csv('Renew.csv')

# Setting a color scheme
colors = plt.cm.Paired(range(len(df_accesstoElec)))
background_color = '#F5F5F5'  # Light gray

# Setting up plot space and axes
fig = plt.figure(figsize=(26, 18), facecolor=background_color)
gs = gridspec.GridSpec(4, 2, width_ratios=[1, 1], height_ratios=[1, 1, 0.1, 0.05])

# Adding the main title for the Plot
plt.suptitle("Environmental Insights (1990-2020): Electricity, CO2, and Conservation",
             fontsize=30, fontweight='bold', y=0.96, color='#228B22')

# Setting a background color
fig.patch.set_facecolor(background_color)

# Plot 1: Access to Electricity Over Time
ax1 = plt.subplot(gs[0, 0])
bar_width = 0.35
index = range(len(df_accesstoElec))
bar1 = ax1.bar(index, df_accesstoElec['1990'], bar_width, 
               label='1990', color=colors[0])
bar2 = ax1.bar([i + bar_width for i in index], df_accesstoElec['2020'],
               bar_width, label='2020', color=colors[1])
ax1.set_title('Access to Electricity Over Time (1990 vs 2020)',
              fontsize=18, fontweight='bold', pad=20, color='#00008B')
ax1.set_ylabel('% of Population with Access', fontsize=14, fontweight='bold')
ax1.set_xlabel('Regions', fontsize=14, fontweight='bold')
ax1.set_xticks([i + bar_width / 2 for i in index])
ax1.set_xticklabels(df_accesstoElec['Region'], ha="right")
ax1.legend()

# Plot 2: Threatened Bird Species by Region (2020)
ax2 = plt.subplot(gs[0, 1])
pie_slices, texts, autotexts = ax2.pie(df_birds['Threatened Species'],
   labels=df_birds['Region'], autopct='%1.1f%%', startangle=140, colors=colors)
ax2.set_title('Threatened Bird Species by Region (2020)',
              fontsize=18, fontweight='bold', pad=20, color='#00008B')
ax2.axis('equal')

# Making the labels bold
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

# Plot 3: Top-10 CO2 Emitting Countries (2020)
ax3 = plt.subplot(gs[1, 0])
df_co2_sorted = df_co2.sort_values(by='Co2 Emission', ascending=False).head(10)
bars = ax3.barh(df_co2_sorted['Country'], df_co2_sorted['Co2 Emission'], 
                color=colors[2])
max_co2_emission = df_co2_sorted['Co2 Emission'].max()
ax3.set_title('Top-10 CO2 Emitting Countries (2020)',
              fontsize=18, fontweight='bold', pad=20, color='#00008B')
ax3.set_xlabel('CO2 Emission (Metric Ton Per Capita)', 
               fontsize=14, fontweight='bold')
ax3.set_ylabel('Countries', fontsize=14, fontweight='bold')
for bar in bars:
    plt.text(
        bar.get_width(),  # Bar length
        bar.get_y() + bar.get_height() / 2,  # Bar position on y-axis
        f'{bar.get_width():.2f}',  # Bar value
        va='center'  # Vertical alignment
    )
ax3.set_xlim(0, max_co2_emission * 1.15)

# Plot 4: Renewable Energy Consumption Over Time
ax4 = plt.subplot(gs[1, 1])
for index, row in df_renew.iterrows():
    ax4.plot(df_renew.columns[1:], row.values[1:], 
             label=row['Row Labels'], color=colors[index])
ax4.set_title('Renewable Energy Consumption Over Time (1990-2020)',
              fontsize=18, fontweight='bold', pad=20, color='#00008B')
ax4.set_ylabel('Renewable Energy Consumption (%)',
               fontsize=14, fontweight='bold')
ax4.set_xlabel('Years', fontsize=14, fontweight='bold')
ax4.legend(bbox_to_anchor=(1, 1), loc='upper left')

formatplot(ax1, 'black')
formatplot(ax2, 'black')
formatplot(ax3, 'black')
formatplot(ax4, 'black')

# Adjust space between plots
plt.subplots_adjust(wspace=10, hspace=10)

# Set the background color for the entire figure
fig.patch.set_facecolor(background_color)

# Enhancing X-ticks
for ax in [ax1, ax3]:
    ax.tick_params(axis='x', labelsize=12, labelrotation=45)
    ax.tick_params(axis='y', labelsize=12)
    for label in ax.get_xticklabels():
        label.set_fontweight('bold')

# For ax4 and ax3, remove the rotation for x-ticks
ax4.tick_params(axis='x', labelsize=12, labelrotation=0)
ax3.tick_params(axis='x', labelsize=12, labelrotation=0)

# Setting up Text block
ax_text = plt.subplot(gs[2, :])  # Spanning the entire third row
ax_text.axis('off')
text_content = (
    "• East Asia & Pacific saw a decrease in electricity access from 99.64% to 92.32% (1990-2020), "
    "with 1,224 threatened bird species indicating additional environmental concerns. "
    "This slight decrease in electricity access, despite a high number of threatened species, suggests other environmental impact factors.\n"
    "• Qatar, Bahrain, and Kuwait have high CO2 emissions (31.73, 21.98, and 21.17 metric tons per capita respectively), "
    "suggesting significant sources of CO2 beyond electricity use. These high levels of emissions, not directly linked to electricity access, indicate significant sources of CO2 in these countries.\n"
    "• Renewable energy usage in Europe & Central Asia increased from 11.03% in 1990 to 23.53% in 2020. "
    "With 678 threatened bird species in the region, this increase in renewable energy usage indicates a positive trend in environmental conservation.\n"
    "• In East Asia & Pacific and Latin America & Caribbean, renewable energy consumption decreased (to 17.55% and 20.71% respectively) "
    "alongside high numbers of threatened bird species, highlighting the need for more investment in renewable energy.\n"
    "• Sub-Saharan Africa faces biodiversity challenges with lower CO2 emissions, indicating that environmental threats are likely due to factors other than emissions, such as habitat destruction."
)

ax_text.text(0, 0.5, text_content,
             ha='left', va='center', fontsize=20, color='black', wrap=True)

# Adding the name and ID in the last row of the grid
ax_name_id = plt.subplot(gs[3, :])  # This is the new row for name and ID
ax_name_id.axis('off')
ax_name_id.text(0.95, 0.5, "Name:Sai Mohan Batta \n ID:22065814 ", ha="right", 
                fontsize=18, color='black')

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()
