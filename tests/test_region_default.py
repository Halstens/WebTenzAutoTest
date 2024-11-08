from pages.sbis_contacts_page import SbisContactsPage

def test_define_region_default(browser):
    sbis_contact = SbisContactsPage(browser)
    sbis_contact.open()
    assert sbis_contact.list_partners_is_displayed() and sbis_contact.span_region_is_displayed()

