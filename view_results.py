#!/usr/bin/env python3
"""
View and analyze face search results
Display statistics and top matches
"""

import os
import json
from config import CONFIG

def load_results():
    """Load results from JSON file"""
    results_file = os.path.join(CONFIG['RESULTS_DIR'], 'results.json')
    
    if not os.path.exists(results_file):
        print(f"✗ Results file not found: {results_file}")
        print("Please run face_search.py first to generate results")
        return None
    
    try:
        with open(results_file, 'r', encoding='utf-8') as f:
            matches = json.load(f)
        return matches
    except Exception as e:
        print(f"✗ Error loading results: {e}")
        return None

def display_statistics(matches):
    """Display statistical information about matches"""
    if not matches:
        print("No matches found")
        return
    
    # Calculate statistics
    similarities = [m['similarity'] for m in matches]
    distances = [m['distance'] for m in matches]
    
    avg_similarity = sum(similarities) / len(similarities)
    max_similarity = max(similarities)
    min_similarity = min(similarities)
    
    avg_distance = sum(distances) / len(distances)
    max_distance = max(distances)
    min_distance = min(distances)
    
    # Count by similarity range
    excellent = len([s for s in similarities if s >= 90])
    good = len([s for s in similarities if 80 <= s < 90])
    fair = len([s for s in similarities if 70 <= s < 80])
    poor = len([s for s in similarities if s < 70])
    
    print("\n" + "="*60)
    print("SEARCH RESULTS STATISTICS")
    print("="*60)
    print(f"\nTotal matches: {len(matches)}")
    print(f"Tolerance used: {CONFIG.get('TOLERANCE', 'N/A')}")
    
    print("\n" + "-"*60)
    print("SIMILARITY SCORES")
    print("-"*60)
    print(f"Average: {avg_similarity:.2f}%")
    print(f"Highest: {max_similarity:.2f}%")
    print(f"Lowest:  {min_similarity:.2f}%")
    
    print("\n" + "-"*60)
    print("FACE DISTANCE")
    print("-"*60)
    print(f"Average: {avg_distance:.4f}")
    print(f"Minimum: {min_distance:.4f}")
    print(f"Maximum: {max_distance:.4f}")
    
    print("\n" + "-"*60)
    print("QUALITY DISTRIBUTION")
    print("-"*60)
    print(f"Excellent (≥90%): {excellent} images ({excellent/len(matches)*100:.1f}%)")
    print(f"Good (80-89%):    {good} images ({good/len(matches)*100:.1f}%)")
    print(f"Fair (70-79%):    {fair} images ({fair/len(matches)*100:.1f}%)")
    print(f"Poor (<70%):      {poor} images ({poor/len(matches)*100:.1f}%)")

def display_top_matches(matches, count=10):
    """Display top N matches"""
    print("\n" + "="*60)
    print(f"TOP {min(count, len(matches))} MATCHES")
    print("="*60)
    
    # Sort by similarity (already sorted, but just to be sure)
    sorted_matches = sorted(matches, key=lambda x: x['similarity'], reverse=True)
    
    print(f"\n{'Rank':<6} {'Similarity':<12} {'Distance':<12} {'Filename'}")
    print("-"*60)
    
    for idx, match in enumerate(sorted_matches[:count], 1):
        similarity = match['similarity']
        distance = match['distance']
        filename = match['file_name']
        
        # Truncate long filenames
        if len(filename) > 35:
            filename = filename[:32] + "..."
        
        # Add visual indicator for quality
        if similarity >= 90:
            indicator = "🟢"
        elif similarity >= 80:
            indicator = "🟡"
        elif similarity >= 70:
            indicator = "🟠"
        else:
            indicator = "🔴"
        
        print(f"{idx:<6} {similarity:>6.2f}% {indicator:<3} {distance:>8.4f}    {filename}")

def display_low_confidence(matches, threshold=70):
    """Display matches below confidence threshold"""
    low_conf = [m for m in matches if m['similarity'] < threshold]
    
    if not low_conf:
        return
    
    print("\n" + "="*60)
    print(f"LOW CONFIDENCE MATCHES (<{threshold}%)")
    print("="*60)
    print(f"\nFound {len(low_conf)} matches with similarity below {threshold}%")
    print("Consider reviewing these manually or adjusting the tolerance")
    
    print(f"\n{'Similarity':<12} {'Filename'}")
    print("-"*60)
    
    for match in sorted(low_conf, key=lambda x: x['similarity']):
        similarity = match['similarity']
        filename = match['file_name']
        
        if len(filename) > 45:
            filename = filename[:42] + "..."
        
        print(f"{similarity:>6.2f}%     {filename}")

def export_file_list(matches, output_file='matched_files.txt'):
    """Export list of matched file names"""
    output_path = os.path.join(CONFIG['RESULTS_DIR'], output_file)
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# Matched Files List\n")
            f.write(f"# Total: {len(matches)} files\n")
            f.write(f"# Sorted by similarity (highest first)\n\n")
            
            for match in matches:
                f.write(f"{match['file_name']}\n")
        
        print(f"\n✓ File list exported to: {output_path}")
    except Exception as e:
        print(f"\n✗ Error exporting file list: {e}")

def main():
    """Main function"""
    print("="*60)
    print("FACE SEARCH RESULTS VIEWER")
    print("="*60)
    
    # Load results
    matches = load_results()
    if matches is None:
        return
    
    # Display all information
    display_statistics(matches)
    display_top_matches(matches, count=15)
    display_low_confidence(matches)
    
    # Export file list
    export_file_list(matches)
    
    print("\n" + "="*60)
    print("For detailed results, see:")
    print(f"  - {os.path.join(CONFIG['RESULTS_DIR'], 'report.txt')}")
    print(f"  - {os.path.join(CONFIG['RESULTS_DIR'], 'results.json')}")
    print("="*60)

if __name__ == "__main__":
    main()
