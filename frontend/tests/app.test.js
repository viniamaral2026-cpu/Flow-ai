const { test, expect } = require('@playwright/test');

test.describe('Main App (Authenticated)', () => {
  test.beforeEach(async ({ page }) => {
    // Simulate being authenticated by setting localStorage
    await page.goto('http://localhost:5173');
    await page.evaluate(() => {
      localStorage.setItem('isAuthenticated', 'true');
      localStorage.setItem('user', JSON.stringify({ name: 'Test User' }));
    });
    await page.reload();
  });

  test('should display main app layout', async ({ page }) => {
    await page.goto('http://localhost:5173');
    
    // Check header elements
    await expect(page.locator('text=Flow AI — Assistente Autônomo')).toBeVisible();
    await expect(page.locator('text=Test User')).toBeVisible();
    await expect(page.locator('text=Sair')).toBeVisible();
    
    // Check sidebar
    await expect(page.locator('text=Principal')).toBeVisible();
    await expect(page.locator('text=Conversas')).toBeVisible();
    await expect(page.locator('text=Ver e Agir')).toBeVisible();
    
    // Check that home screen is visible by default
    await expect(page.locator('text=Flow AI v3.0')).toBeVisible();
  });

  test('should navigate to chat screen', async ({ page }) => {
    await page.goto('http://localhost:5173');
    
    await page.click('text=Conversas');
    
    await expect(page.locator('text=Pergunte algo...')).toBeVisible();
    await expect(page.locator('text=Olá! Sou a Flow')).toBeVisible();
  });

  test('should navigate to timers screen', async ({ page }) => {
    await page.goto('http://localhost:5173');
    
    await page.click('text=Timers e Alarmes');
    
    await expect(page.locator('text=Timers e Alarmes')).toBeVisible();
    await expect(page.locator('text=Crie timers com nome')).toBeVisible();
  });
});