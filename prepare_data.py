import pandas as pd
import os

# Load real news
real_df = pd.read_csv('dataset/Real.csv')
real_df['label'] = 1  # Real
real_df = real_df[['title', 'text', 'label']].rename(columns={'title': 'headline', 'text': 'text'})

# Load fake news (assuming it's in dataset/fake.csv/fake.csv)
fake_df = pd.read_csv('dataset/fake.csv/fake.csv')
fake_df['label'] = 0  # Fake
fake_df = fake_df[['title', 'text', 'label']].rename(columns={'title': 'headline', 'text': 'text'})

# Combine
combined_df = pd.concat([real_df, fake_df], ignore_index=True)

# Save
combined_df.to_csv('train_combined_new.csv', index=False)

print(f"Combined dataset saved with {len(combined_df)} samples")
print(combined_df.head())