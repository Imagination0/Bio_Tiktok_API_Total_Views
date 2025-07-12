from tiktok_api import update_tiktok_bio, get_total_views

def main():
    total_views = get_total_views()
    bio_text = f"📊 Total Views: {total_views}"
    update_tiktok_bio(bio_text)

if __name__ == "__main__":
    main()
