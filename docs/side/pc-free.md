# Using a PC to Sideload Apps onto Your Device

This is the most common and beginner-friendly and completely free sideloading method.  
It uses your Apple ID certificate to install apps without a developer account.  
Links to the apps and tools that are required can be found at the [Recommended Tools](#recommended-tools) section. 
Just choose a method and it will bring you to a instructions page on how to install it.

---

## Requirements
- **Windows or macOS**, sadly no Linux support yet, linux doesnt have iTunes or iCloud whitch is both needed.
- **iTunes** *(desktop version — not the Microsoft Store one)*  
- **Old iCloud app** *(needed for Apple services integration)*
- **A USB cable**
- **Your Apple ID login credentials**
- And whatever additional tool that is needed for the method you choose.

---

## Additional Info & Limitations
- Keep in mind, if for some reason you can't install the required apps on your PC or don't want to get rid of the iCloud from the Microsoft store, you can also just make a windows 10 or 11 virtual machine.
- Your Apple ID acts as your **signing certificate**. 
- There are also app ID's but i dont fully get either you can always go look it up on the [respective subreddits.](/side/#respective-subreddits)
- You can sideload **only 3 apps** at a time using a free Apple ID.  
- Apps must be **re-signed every 7 days** to remain functional.   
- **Push notifications** and **in-app link opening** (e.g., https://reddot.com → Reddit app) are not supported. What will work are URI schemes (e.g., reddit:// → Reddit app). 
- Depending on the method you choose the device must be **connected to the computer** during the sideloading process.

---

## Recommended Tools

### [**AltStore**](https://altstore.io)

Here is the documentation on how to install AltStore: [AltStore Installation Guide](https://faq.altstore.io/altstore-classic/how-to-install-altstore-windows)

- AltStore will install a separate AltStore app onto your device so it's easier to refresh and manage your apps.
- Sadly the app itself counts as **1 of your 3** available app slots.
- With AltStore app you can deactivate other apps to free up your limited app slots. (Deactivating will keep the apps data)
- Easiest to use but tedious to maintain because you have to refresh apps every 7 days while you are connected to your PC.
- If you're lucky your device will still show up over the wifi network, so you dont have to plug it in every time.


### [**SideStore**](https://sidestore.io/)

Simply click on the "Get Started" button on the website to see the instructions.

- Like AltStore, SideStore installs a separate app onto your device to manage your sideloaded apps.
- The SideStore app counts as **1 of your 3** available app slots.
- With SideStore app you can deactivate other apps to free up your limited app slots. (Deactivating will keep the apps data)
- Takes a bit of time to set up but is really easy to use afterwards.
- The biggest difference with SideStore is, you dont need to be connected to a PC to refresh your apps, you only need a PC to install SideStore in the beginning.
- To be able to refresh and install apps without a PC you will need to configure a pairing file and be connected with StosVPN. Everything is explained in the instructions on the website.


### [**Sideloadly**](https://sideloadly.io/)

For the installation instructions you would need to find them, theres a tutorial tab on the website that leads you to a youtube video, but you can also just search for it on the [respective subreddit.](/side/#respective-subreddits)

- Sideloadly would be the most basic method of the three. 
- The **three app slots limitation** still applies. Sideloadly isnt a physical app on your device, its just an app on your PC. So you can use all 3 app slots for other apps.
- Sideloadly has a lot of customization options, like changing the app name, bundle identifier and even the app icon.
- If you wish to edit the app but not install it you can do so by turning on the export IPA option.

---

## Tips
- Try to **refresh apps** every few days to avoid it expiring after **7 days**.
- As a tool to avoid **limiting your self to only three apps** you can use [LiveContainer](https://github.com/LiveContainer/LiveContainer). (For more information try searching for it on the [respective subreddit.](/side/#respective-subreddits))
- With LiveContainer you can install unlimited apps, it acts like a VM for apps.
- With SideStore you can install the [LiveContainer+SideStore](https://github.com/LiveContainer/LiveContainer/releases) combination so you can free up a app slot and use LiveContainer in its place.

---

## Summary

Using a PC to sideload is the **best starting point**:

- It’s **free**.
- It’s **safe** (your Apple ID is Sadly stored).
- And it's **cool** to learn how the signing process works.
