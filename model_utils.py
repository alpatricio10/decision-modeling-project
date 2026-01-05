import pandas as pd
import numpy as np

def load_food_database(filepath):
    """Load the food database from Excel file"""
    df = pd.read_excel(filepath)
    print(f"Database loaded: {len(df)} products")
    return df

def validate_database(df):
    """
    Validate database against project requirements:
    - At least 200 foods
    - Each Nutri-Score label (A-E) has at least 15% representation
    - Each Green-Score label (A-E) has at least 10% representation
    """
    print("\n=== DATABASE VALIDATION ===")
    n_products = len(df)
    print(f"Total products: {n_products}")
    
    # Check minimum size
    if n_products < 200:
        print("⚠️  WARNING: Database has fewer than 200 products")
    else:
        print("✓ Database size requirement met")
    
    # Check Nutri-Score distribution
    print("\nNutri-Score Distribution:")
    if 'nutri_score_label' in df.columns:
        nutri_counts = df['nutri_score_label'].value_counts()
        nutri_pct = (nutri_counts / n_products * 100).round(2)
        for label in ['A', 'B', 'C', 'D', 'E']:
            pct = nutri_pct.get(label, 0)
            status = "✓" if pct >= 15 else "⚠️"
            print(f"  {status} Class {label}: {nutri_counts.get(label, 0)} ({pct}%)")
    else:
         print("⚠️  WARNING: 'nutri_score_label' column not found")
    
    # Check Green-Score distribution
    print("\nGreen-Score Distribution:")
    if 'green_score_label' in df.columns:
        green_counts = df['green_score_label'].value_counts()
        green_pct = (green_counts / n_products * 100).round(2)
        for label in ['A', 'B', 'C', 'D', 'E']:
            pct = green_pct.get(label, 0)
            status = "✓" if pct >= 10 else "⚠️"
            print(f"  {status} Class {label}: {green_counts.get(label, 0)} ({pct}%)")
    else:
        print("⚠️  WARNING: 'green_score_label' column not found")

def compare_databases(df1, df2):
    """
    Compare two databases to ensure less than 30% overlap by product name
    """    
    # Compare by product name
    products1 = set(df1['product_name'].str.lower().str.strip())
    products2 = set(df2['product_name'].str.lower().str.strip())
    
    common = products1.intersection(products2)
    overlap_pct = len(common) / max(len(products1), len(products2)) * 100
    
    print(f"\n=== DATABASE COMPARISON ===")
    print(f"Database 1: {len(products1)} products")
    print(f"Database 2: {len(products2)} products")
    print(f"Common products: {len(common)} ({overlap_pct:.2f}%)")
    
    if overlap_pct <= 30:
        print("✓ Overlap requirement met (≤30%)")
        # return True
    else:
        print("⚠️  WARNING: Overlap exceeds 30%")
        # return False
