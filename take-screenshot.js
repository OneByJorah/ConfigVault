const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: true,
    executablePath: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH || '/usr/bin/chromium-browser'
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:5000/');
  await page.waitForTimeout(3000);
  await page.screenshot({ path: '/home/j1coder/configvault-screenshot.png', fullPage: true });
  await browser.close();
  console.log('Screenshot saved!');
})();
