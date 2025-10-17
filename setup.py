#!/usr/bin/env python3
"""
Setup script for Face Recognition Search Tool
Helps users configure the tool for first-time use
"""

import os
import sys

def check_requirements():
    """Check if all required packages are installed"""
    print("Checking requirements...")
    try:
        import face_recognition
        import cv2
        import numpy
        import PIL
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
        from tqdm import tqdm
        print("✓ All required packages are installed")
        return True
    except ImportError as e:
        print(f"✗ Missing package: {e}")
        print("\nPlease install requirements:")
        print("pip install -r requirements.txt")
        return False

def setup_config():
    """Interactive configuration setup"""
    print("\n" + "="*60)
    print("FACE RECOGNITION SEARCH TOOL - SETUP")
    print("="*60 + "\n")
    
    # Check if config.py exists
    if not os.path.exists('config.py'):
        print("✗ config.py not found!")
        return False
    
    # Check credentials
    if not os.path.exists('credentials.json'):
        print("⚠ credentials.json not found")
        print("\nTo get credentials:")
        print("1. Go to Google Cloud Console")
        print("2. Enable Google Drive API")
        print("3. Create a service account")
        print("4. Download JSON key and save as credentials.json")
        print("\nSee README.md for detailed instructions")
        
        has_creds = input("\nDo you have credentials.json ready? (y/n): ").lower()
        if has_creds != 'y':
            return False
    else:
        print("✓ credentials.json found")
    
    # Get folder ID
    print("\n" + "-"*60)
    print("GOOGLE DRIVE FOLDER CONFIGURATION")
    print("-"*60)
    folder_id = input("\nEnter your Google Drive folder ID: ").strip()
    
    if not folder_id:
        print("✗ Folder ID is required")
        return False
    
    # Update config.py
    try:
        with open('config.py', 'r') as f:
            config_content = f.read()
        
        config_content = config_content.replace(
            "'DRIVE_FOLDER_ID': 'your_folder_id_here'",
            f"'DRIVE_FOLDER_ID': '{folder_id}'"
        )
        
        with open('config.py', 'w') as f:
            f.write(config_content)
        
        print(f"✓ Updated config.py with folder ID: {folder_id}")
    except Exception as e:
        print(f"✗ Error updating config.py: {e}")
        return False
    
    # Check target image
    print("\n" + "-"*60)
    print("TARGET IMAGE CONFIGURATION")
    print("-"*60)
    
    if not os.path.exists('target_person.jpg'):
        print("⚠ target_person.jpg not found")
        print("\nPlease add a clear photo of the person you want to find.")
        print("Save it as 'target_person.jpg' in this directory.")
        
        has_image = input("\nDo you have the target image ready? (y/n): ").lower()
        if has_image != 'y':
            print("\nPlease add target_person.jpg and run setup again")
            return False
    else:
        print("✓ target_person.jpg found")
    
    # All checks passed
    print("\n" + "="*60)
    print("✓ SETUP COMPLETE!")
    print("="*60)
    print("\nYou can now run the face search:")
    print("python face_search.py")
    
    return True

def main():
    """Main setup function"""
    print("\nFace Recognition Search Tool - Setup")
    print("=" * 60)
    
    # Check requirements first
    if not check_requirements():
        sys.exit(1)
    
    # Run configuration setup
    if not setup_config():
        print("\n✗ Setup incomplete. Please fix the issues and run setup again.")
        sys.exit(1)
    
    print("\n✓ Setup successful! You're ready to go.")

if __name__ == "__main__":
    main()
