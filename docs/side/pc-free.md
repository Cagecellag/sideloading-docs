# Using a PC to Sideload Apps onto Your Device

This is the most common, beginner-friendly, and completely free sideloading method.  
It uses your Apple ID certificate to install apps without a developer account.  
Links to the required apps and tools can be found in the [Recommended Tools](#recommended-tools) section. 
Just choose a method and it will bring you to an instructions page on how to install it.

---

## Requirements
- **Windows or macOS** (sadly, no Linux support yet; Linux doesn't have iTunes or iCloud, which are both needed)
- **iTunes** *(desktop version — not the Microsoft Store version)*  
- **Old iCloud app** *(needed for Apple services integration)*
- **A USB cable**
- **Your Apple ID login credentials**
- Any additional tool required for the method you choose.

---

## Additional Info & Limitations
- Keep in mind, if for some reason you can't install the required apps on your PC or don't want to remove iCloud from the Microsoft Store, you can also create a Windows 10 or 11 virtual machine.
- Your Apple ID acts as your **signing certificate**. 
- There are also app IDs, but I don't fully understand them; you can always look them up on the [respective subreddits.](/side/#respective-subreddits)
- You can sideload **only 3 apps** at a time using a free Apple ID.  
- Apps must be **re-signed every 7 days** to remain functional.   
- **Push notifications** and **in-app link opening** (e.g., https://reddot.com → Reddit app) are not supported. However, URI schemes (e.g., reddit:// → Reddit app) will work. 
- Depending on the method you choose, the device must be **connected to the computer** during the sideloading process.

---

## Recommended Tools

### [**AltStore**](https://altstore.io)

Here is the documentation on how to install AltStore: [AltStore Installation Guide](https://faq.altstore.io/altstore-classic/how-to-install-altstore-windows)

- AltStore will install a separate AltStore app onto your device so it's easier to refresh and manage your apps.
- Sadly the app itself counts as **1 of your 3** available app slots.
- With the AltStore app, you can deactivate other apps to free up your limited app slots (deactivating will keep the app's data).
- It's the easiest to use but tedious to maintain because you have to refresh apps every 7 days while connected to your PC.
- If you're lucky, your device will still show up over the Wi-Fi network, so you don't have to plug it in every time.


### [**SideStore**](https://sidestore.io/)

Simply click on the "Get Started" button on the website to see the instructions.

- Like AltStore, SideStore installs a separate app onto your device to manage your sideloaded apps.
- The SideStore app counts as **1 of your 3** available app slots.
- With the SideStore app, you can deactivate other apps to free up your limited app slots (deactivating will keep the app's data).
- It takes a bit of time to set up but is really easy to use afterward.
- The biggest difference with SideStore is that you don't need to be connected to a PC to refresh your apps; you only need a PC to install SideStore initially.
- To refresh and install apps without a PC, you will need to configure a pairing file and be connected with StosVPN. Everything is explained in the instructions on the website.


### [**Sideloadly**](https://sideloadly.io/)

For installation instructions, use the tutorial tab on the website, which leads to a YouTube video, or search for it on the [respective subreddit.](/side/#respective-subreddits)

- Sideloadly is the most basic method of the three. 
- The **three app slots limitation** still applies. Sideloadly isn't a physical app on your device; it's just an app on your PC, so you can use all 3 app slots for other apps.
- Sideloadly has many customization options, like changing the app name, bundle identifier, and even the app icon.
- If you wish to edit the app but not install it, you can do so by turning on the export IPA option.

---

## Tips
- Try to **refresh apps** every few days to avoid them expiring after **7 days**.
- To avoid **limiting yourself to only three apps**, you can use [LiveContainer](https://github.com/LiveContainer/LiveContainer). (For more information, try searching for it on the [respective subreddit.](/side/#respective-subreddits))
- With LiveContainer, you can install unlimited apps; it acts like a VM for apps.
- With SideStore, you can install the [LiveContainer+SideStore](https://github.com/LiveContainer/LiveContainer/releases) combination so you can free up an app slot and use LiveContainer in its place.

---

## Summary

Using a PC to sideload is the **best starting point**:

- It’s **free**.
- It’s **safe** (although your Apple ID is unfortunately stored).
- And it's **interesting** to learn how the signing process works.
