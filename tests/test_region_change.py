from pages.sbis_contacts_page import SbisContactsPage

def test_region_change(browser):
    sbis_contact = SbisContactsPage(browser)
    sbis_contact.open()
    sbis_contact.span_region_click()
    sbis_contact.searching_region_click()
    assert sbis_contact.title_url_page() and sbis_contact.updated_span_region_is_displayed() and sbis_contact.check_partner_is_displayed()