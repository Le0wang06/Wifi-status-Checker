import speedtest

def test_wifi_speed():
    print("Starting WiFi speed test...")  # Debug print

    wifi = speedtest.Speedtest()
    print("Getting best server...")  # Debug print

    wifi.get_best_server()
    print("Running download speed test...")  # Debug print

    download_speed = wifi.download() / 1_000_000  # Convert from bps to Mbps
    print("Download test completed.")  # Debug print

    print("Running upload speed test...")  # Debug print
    upload_speed = wifi.upload() / 1_000_000  # Convert from bps to Mbps
    print("Upload test completed.")  # Debug print

    # Display the results
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

# Run the function to test WiFi speed
if __name__ == "__main__":
    test_wifi_speed()
