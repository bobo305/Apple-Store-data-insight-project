import matplotlib.pyplot as plt
import numpy as np


unique_apps_counts = [7197, 7197]
missing_values_counts = [0]
genres = ["Games", "Entertainment", "Education", "Photos & Video", "Utilities", "Health & Fitness", "Productivity",
          "Social Networking", "Lifestyle", "Music", "Shopping", "Sports", "Books", "Finance", "Travel", "News",
          "Weather", "Reference", "Food & Drink", "Business", "Navigation", "Medical", "Catalogs"]
num_apps = [3862, 535, 453, 349, 248, 180, 178, 167, 144, 138, 122, 114, 112, 104, 81, 75, 72, 64, 63, 57, 46, 23, 10]
user_ratings = [0, 3.5, 5]
paid_vs_free_ratings = [3.7, 3.37]
supported_languages = ["<10", "10-30", ">30"]
avg_ratings_languages = [3.7, 4.1, 3.7]
low_rated_genres = ["Catalogs", "Finance", "Books", "Navigation", "Lifestyle", "News", "Sports",
                    "Social Networking", "Food & Drink", "Entertainment", "Utilities", "Medical", "Education", "Travel",
                    "Reference", "Shopping", "Weather", "Games", "Health & Fitness", "Business", "Photo & Video", "Music",
                    "Productivity"]
avg_ratings_low_rated = [2.1, 2.43, 2.47, 2.68, 2.8, 2.98, 2.98, 2.98, 3.18, 3.23, 3.27, 3.36, 3.37, 3.37, 3.45, 3.54,
                        3.59, 3.68, 3.7, 3.74, 3.8, 3.97, 4.0]
description_lengths = ["Short", "Medium", "Long"]
avg_ratings_lengths = [2.53, 3.23, 3.85]
# top_rated_apps = [("Books", "Color Therapy Adult Coloring Book for Adults", 5),
#                   ("Business", "TurboScan™ Pro", 5),
#                   ("Catalogs", "CPlus for Craigslist app", 5),
#                   ("Education", "Elevate", 5),
#                   ("Entertainment", "Bruh-Button", 5),
#                   ("Finance", "Credit Karma", 5),
#                   ("Food & Drink", "Domino's Pizza USA", 5),
#                   ("Games", "Head Soccer", 5),
#                   ("Health & Fitness", "Yoga Studio", 5),
#                   ("Lifestyle", "ipsy", 5),
#                   ("Medical", "Blink Health", 5),
#                   ("Music", "Tenuto", 5),
#                   ("Navigation", "parkOmator", 5),
#                   ("News", "The Guardian", 5),
#                   ("Photo & Video", "Pic Collage", 5),
#                   ("Productivity", "VPN Proxy Master", 5),
#                   ("Reference", "Sky Guide", 5),
#                   ("Shopping", "Zappos", 5),
#                   ("Social Networking", "We Heart It", 5),
#                   ("Sports", "J23", 5),
#                   ("Travel", "Urlaubspiraten", 5),
#                   ("Utilities", "Flashlight ", 5),
#                   ("Weather", "NOAA Hi-Def Radar Pro", 5)]

# # Extract genre and app names for labeling
# genre_names, app_names, ratings = zip(*top_rated_apps)

# Create subplots with a larger figure size and improved spacing
fig, axs = plt.subplots(3, 3, figsize=(15, 15))
fig.suptitle("Apple Store Data Analysis", fontsize=16)

# Subplot 1: Number of Unique Apps
axs[0, 0].pie(unique_apps_counts, labels=["Original Data", "Combined Data"], autopct='%1.1f%%')
axs[0, 0].set_title("Number of Unique Apps")

# Subplot 2: Missing Values
axs[0, 1].bar(["Original Data", "Combined Data"], missing_values_counts)
axs[0, 1].set_title("Missing Values")
axs[0, 1].set_ylabel("Count")

# Subplot 3: Number of Apps per Genre
axs[0, 2].barh(genres, num_apps, color='skyblue')
axs[0, 2].set_xlabel("Number of Apps")
axs[0, 2].set_title("Number of Apps per Genre")

# Subplot 4: Overview of App Ratings
axs[1, 0].hist(user_ratings, bins=5, edgecolor='black', color='lightcoral')
axs[1, 0].set_xlabel("User Ratings")
axs[1, 0].set_ylabel("Frequency")
axs[1, 0].set_title("Distribution of User Ratings")

# Subplot 5: Paid vs. Free Apps Ratings
axs[1, 1].bar(["Paid", "Free"], paid_vs_free_ratings, color=['gold', 'mediumseagreen'])
axs[1, 1].set_ylabel("Average Rating")
axs[1, 1].set_title("Paid vs. Free Apps Ratings")
axs[1, 1].legend(["Paid", "Free"], loc='upper right')


# Subplot 6: Apps Supported Languages vs. Ratings
axs[1, 2].bar(supported_languages, avg_ratings_languages, color='dodgerblue')
axs[1, 2].set_ylabel("Average Rating")
axs[1, 2].set_title("Supported Languages vs. Ratings")

# Subplot 7: Genres with Low Ratings (Polar Plot)
axs[2, 0].remove()
axs[2, 0] = fig.add_subplot(3, 3, 7, polar=True)

theta = np.linspace(0, 2 * np.pi, len(low_rated_genres), endpoint=False)
ratings = avg_ratings_low_rated
width = 0.5
bars = axs[2, 0].bar(theta, ratings, width=width, align="center", color='salmon')
axs[2, 0].set_xticks(theta)
axs[2, 0].set_xticklabels(low_rated_genres, rotation=45, fontsize=8)
axs[2, 0].set_title("Genres with Low Ratings (Polar Plot)")

# Subplot 8: App Description Length vs. User Rating
axs[2, 1].bar(description_lengths, avg_ratings_lengths, color='lightseagreen')
axs[2, 1].set_ylabel("Average Rating")
axs[2, 1].set_title("App Description Length vs. User Rating")

# Removing subplot 9 (empty subplot)
fig.delaxes(axs[2, 2])

for ax in axs.flat:
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.set_xticklabels(ax.get_xticklabels(), fontsize=10)

plt.tight_layout(rect=[0, 0, 1, 0.96])


# option to save  the figure as an image file for sharing or further analysis
plt.savefig("apple_store_analysis.png", dpi=300, bbox_inches='tight')

# Display the figure
plt.show()