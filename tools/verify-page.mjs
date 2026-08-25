import { chromium } from 'playwright'

const browser = await chromium.launch()
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } })

page.on('console', msg => console.log('PAGE LOG:', msg.text()))
page.on('pageerror', err => console.log('PAGE ERROR:', err.message))

await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' })
await page.waitForTimeout(1500)

// Take screenshot of hero
await page.screenshot({ path: 'tools/out/hero-test.png' })
console.log('Hero captured')

// Scroll to #intro
const introEl = await page.$('#intro')
if (introEl) {
  await introEl.scrollIntoViewIfNeeded()
  await page.waitForTimeout(2000)
  await page.screenshot({ path: 'tools/out/intro-test.png' })
  console.log('Intro captured')
}

// Scroll to NameStrip (section with marquee)
await page.evaluate(() => {
  const el = document.querySelector('section[aria-label*="FARHAAN"]') || document.querySelectorAll('section')[2]
  if (el) el.scrollIntoView()
})
await page.waitForTimeout(2000)
await page.screenshot({ path: 'tools/out/namestrip-test.png' })
console.log('NameStrip captured')

await browser.close()
