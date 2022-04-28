describe('Homepage End-to-end Test', () => {

    it('test home page should be loaded', browser => {
        browser
            .navigateTo('http://localhost:8080')
            .assert.visible('#app')
            .expect.elements('.container').count.toEqual(1);
    });

    it('test should navigate to company view', browser => {
        browser
            .click('link text', 'Add Company')
            .assert.textEquals('.heading', 'CompanyView');
    });

    it('test should create company', browser => {
        browser
            .setValue('input[name="name"]', 'Name')
            .setValue('input[name="office"]', 'Office')
            .setValue('input[name="contact"]', 'Contact')
            .setValue('input[name="phone-number"]', '+555777444555')
            .click('button[type=submit]')
            .assert.visible('button[name="remove-company"]');
    });

    it('test should navigate to shipment view', browser => {
        browser
            .click('link text', 'Add Shipment')
            .assert.textEquals('.heading', 'ShipmentView');
    });

    it('test should create shipment', browser => {
        browser
            .setValue('input[name="recipient"]', 'Recipient')
            .setValue('input[name="destination"]', 'Destination')
            .setValue('textarea[name="description"]', 'Description')
            .setValue('input[name="contact-phone"]', '+555777444555')
            .waitForElementVisible('button[type=submit]')
            .assert.visible('button[type=submit]')
            .click('button[type=submit]')
            .assert.textEquals('.error-message', 'Please add at least one cargo')
            .click('button[name=add-cargo]')
            .waitForElementVisible('input[name="cargo-volume-m3"]')
            .assert.visible('input[name="cargo-volume-m3"]')
            .setValue('input[name="cargo-volume-m3"]', '50')
            .setValue('input[name="cargo-weight-kg"]', '0.5')
            .setValue('input[name="cargo-name"]', 'Cargo Name')
            .setValue('select[id="company-select"]','Name')
            .waitForElementVisible('button[type=submit]')
            .click('button[type=submit]')
            .assert.visible('button[name="remove-shipment"]');
    });

    it('test should edit shipment', browser => {
        browser
            .click('link text', 'Shipments')
            .assert.textEquals('.heading', 'Home view goes here')
            .useXpath()
            .click("//li[contains(text(), 'Destination - Description')]")
            .useCss()
            .click('link text', 'Edit')
            .assert.textEquals('.heading', 'ShipmentView')
            .setValue('input[name="destination"]', 'DestinationNew')
            .waitForElementVisible('button[type=submit]')
            .assert.visible('button[type=submit]')
            .click('button[type=submit]')
            .click('link text', 'Shipments')
            .assert.textEquals('.heading', 'Home view goes here')
            .useXpath()
            .click("//li[contains(text(), 'DestinationNew - Description')]")
            .useCss()
            .expect.elements('.shipment-details').count.toEqual(1)
            .click('link text', 'Edit')
            .click('button[name="remove-shipment"]')
    });

    after(browser => browser.end());
});