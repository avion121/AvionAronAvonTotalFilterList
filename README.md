# AvionAronAvonTotalFilterList 🛡️

Welcome to the **AvionAronAvonTotalFilterList** repository! This project automatically compiles multiple ad-blocking and privacy filter lists into a single unified list named **AvionAronAvonTotalFilterList**. 
The list is updated daily and can be used across browsers, extensions, Android, and iOS.

---

## What’s Included?

This repository combines the following popular filter lists into one:

1. **Hagezi Pro** - Blocks ads, trackers, and malware.
2. **StevenBlack (Fakenews + Gambling)** - Blocks fake news and gambling sites.
3. **OISD Big List** - A huge list for blocking ads and trackers.
4. **EasyList** - The most popular list for blocking ads.
5. **EasyPrivacy** - Blocks tracking and analytics scripts.
6. **1Hosts Lite** - A lightweight blocklist for ads and trackers.

All these lists are merged into a single file called `AvionAronAvonTotalFilterList.txt`, which is updated **every day at 10:30 AM IST (5:00 AM UTC)**.

---

## How Does It Work?

This repository uses a **GitHub Actions workflow** (an automation tool) to:
1. Download the latest versions of the filter lists.
2. Combine them into one file.
3. Save the file in this repository.

You don’t need to do anything—the list is automatically updated for you!

---

## How to Use the Compiled List

You can use the compiled filter list in your favorite ad-blocking tool or browser extension. Here’s how:

### For Browsers and Extensions:
1. Add the following URL to your ad blocker:

   `https://raw.githubusercontent.com/avion121/AvionAronAvonTotalFilterList/refs/heads/main/AvionAronAvonTotalFilterList.txt`

### For Android:

1. **AdGuard (Android)**
   - Download AdGuard from the official website (since it's not available on the Google Play Store).
   - Open AdGuard and go to **Settings**.
   - Tap **Filters** and then **Custom filters**.
   - Tap the "+" icon to add a new filter.
   - Select **Add custom filter**.
   - Paste the URL of the filter list:  
     `https://raw.githubusercontent.com/avion121/AvionAronAvonTotalFilterList/refs/heads/main/AvionAronAvonTotalFilterList.txt`
   - Tap **Save** and enable the filter.

2. **Blokada (Android)**
   - Download Blokada from the official website or F-Droid.
   - Open Blokada and go to the **Filters** tab.
   - Tap **Add new** at the bottom.
   - Choose **Add URL** and paste the URL of the filter list.
   - Tap **Add** to apply the filter.

3. **DNS66 (Android)**
   - Download DNS66 from F-Droid.
   - Open DNS66 and go to **Filter Lists**.
   - Tap the **+** icon and choose **Add custom filter**.
   - Paste the URL of the filter list.
   - Tap **OK** to save.

### For iOS:

1. **AdGuard (iOS)**
   - Download AdGuard from the App Store.
   - Open AdGuard and go to **Settings**.
   - Tap **Filters** and then **Custom Filters**.
   - Tap **Add Custom Filter** and paste the URL of the filter list:  
     `https://raw.githubusercontent.com/avion121/AvionAronAvonTotalFilterList/refs/heads/main/AvionAronAvonTotalFilterList.txt`
   - Save and enable the filter.

2. **1Blocker (iOS)**
   - Install 1Blocker from the App Store.
   - Open 1Blocker and go to **Settings**.
   - Tap **Custom Lists**.
   - Add a new list by pasting the URL of the filter list.
   - Enable the list for the changes to take effect.

3. **AdGuard DNS (iOS)**
   - If you want to apply the filter list via DNS:
   - Open **Settings** on your iPhone/iPad.
   - Go to **Wi-Fi** and tap the information icon next to the network you're connected to.
   - Scroll down to **Configure DNS**, and set it to **Manual**.
   - Add AdGuard's DNS servers or custom DNS servers that support the custom filter list.
   - The filter list will be applied through DNS over HTTPS.

---

## Why Use This?

- **Saves Time**: Instead of adding multiple filter lists manually, you get everything in one place.
- **Always Updated**: The list is updated daily, so you’re always protected.
- **Easy to Use**: Just add one URL to your ad blocker, and you’re done!

---

## Repository Structure

Here’s what’s inside this repository:

- `.github/workflows/compile_filters.yml`: The automation script that runs daily.
- `compile_filter_lists.py`: The Python script that downloads and combines the filter lists.
- `AvionAronAvonTotalFilterList.txt`: The final compiled list (updated daily).

---

## Need Help or Have Suggestions?

If you have any questions, suggestions, or run into issues:
1. Open an issue in this repository.
2. Describe your problem or idea.
3. I’ll get back to you as soon as possible!

---

## License

This project is open-source and licensed under the **MIT License**. 
Feel free to use the compiled filter list, but please respect the license terms. See the [LICENSE](LICENSE) file for details.

---

Enjoy a cleaner, faster, and safer browsing experience! 🚀
