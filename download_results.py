#!/usr/bin/env python3
"""
Download matched images from Google Drive
This script downloads all images that were found to match the target face
"""

import os
import json
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from tqdm import tqdm
from config import CONFIG

def authenticate_drive():
    """Authenticate with Google Drive API"""
    try:
        credentials = service_account.Credentials.from_service_account_file(
            CONFIG['CREDENTIALS_FILE'],
            scopes=['https://www.googleapis.com/auth/drive.readonly']
        )
        service = build('drive', 'v3', credentials=credentials)
        print("✓ Connected to Google Drive API")
        return service
    except Exception as e:
        print(f"✗ Authentication error: {e}")
        return None

def download_file(service, file_id, file_name, output_dir):
    """Download a single file from Google Drive"""
    try:
        request = service.files().get_media(fileId=file_id, supportsAllDrives=True)
        file_path = os.path.join(output_dir, file_name)
        
        with open(file_path, 'wb') as f:
            downloader = MediaIoBaseDownload(f, request)
            done = False
            while not done:
                _, done = downloader.next_chunk()
        
        return True
    except Exception as e:
        print(f"  ✗ Error downloading {file_name}: {e}")
        return False

def main():
    """Main function"""
    print("="*60)
    print("DOWNLOAD MATCHED IMAGES")
    print("="*60)
    
    # Check if results exist
    results_file = os.path.join(CONFIG['RESULTS_DIR'], 'results.json')
    if not os.path.exists(results_file):
        print(f"✗ Results file not found: {results_file}")
        print("Please run face_search.py first to generate results")
        return
    
    # Load results
    try:
        with open(results_file, 'r', encoding='utf-8') as f:
            matches = json.load(f)
        print(f"✓ Loaded {len(matches)} matched images")
    except Exception as e:
        print(f"✗ Error loading results: {e}")
        return
    
    if not matches:
        print("No matched images to download")
        return
    
    # Create download directory
    download_dir = os.path.join(CONFIG['RESULTS_DIR'], 'downloaded_images')
    os.makedirs(download_dir, exist_ok=True)
    print(f"✓ Download directory: {download_dir}")
    
    # Authenticate
    service = authenticate_drive()
    if not service:
        return
    
    # Download images
    print(f"\n📥 Downloading {len(matches)} images...")
    success_count = 0
    
    for match in tqdm(matches, desc="Downloading", unit="image"):
        file_id = match['file_id']
        file_name = match['file_name']
        similarity = match['similarity']
        
        # Add similarity to filename
        name_parts = os.path.splitext(file_name)
        new_name = f"{name_parts[0]}_sim{similarity:.1f}{name_parts[1]}"
        
        if download_file(service, file_id, new_name, download_dir):
            success_count += 1
    
    print(f"\n✓ Successfully downloaded {success_count}/{len(matches)} images")
    print(f"✓ Images saved to: {download_dir}")

if __name__ == "__main__":
    main()
