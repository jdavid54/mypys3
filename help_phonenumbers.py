
# FUNCTIONS
#     can_be_internationally_dialled(numobj)
#         Returns True if the number can only be dialled from outside the region,
#         or unknown.
#         
#         If the number can only be dialled from within the region
#         as well, returns False. Does not check the number is a valid number.
#         Note that, at the moment, this method does not handle short numbers (which
#         are currently all presumed to not be diallable from outside their country).
#         
#         Arguments:
#         numobj -- the phone number objectfor which we want to know whether it is
#                   diallable from outside the region.
#     
#     connects_to_emergency_number(number, region_code)
#         Returns whether the given number, exactly as dialled, might be used to
#         connect to an emergency service in the given region.
#         
#         This function accepts a string, rather than a PhoneNumber, because it
#         needs to distinguish cases such as "+1 911" and "911", where the former
#         may not connect to an emergency service in all cases but the latter would.
#         
#         This function takes into account cases where the number might contain
#         formatting, or might have additional digits appended (when it is okay to
#         do that in the specified region).
#         
#         Arguments:
#         number -- The phone number to test.
#         region_code -- The region where the phone number is being dialed.
#         
#         Returns whether the number might be used to connect to an emergency
#         service in the given region.
#     
#     convert_alpha_characters_in_number(number)
#         Convert alpha chars in a number to their respective digits on a keypad,
#         but retains existing formatting.
#     
#     country_code_for_region(region_code)
#         Returns the country calling code for a specific region.
#         
#         For example, this would be 1 for the United States, and 64 for New
#         Zealand.
#         
#         Arguments:
#         region_code -- The region that we want to get the country calling code for.
#         
#         Returns the country calling code for the region denoted by region_code.
#     
#     country_code_for_valid_region(region_code)
#         Returns the country calling code for a specific region.
#         
#         For example, this would be 1 for the United States, and 64 for New
#         Zealand.  Assumes the region is already valid.
#         
#         Arguments:
#         region_code -- The region that we want to get the country calling code for.
#         
#         Returns the country calling code for the region denoted by region_code.
#     
#     country_mobile_token(country_code)
#         Returns the mobile token for the provided country calling code if it has one, otherwise
#         returns an empty string. A mobile token is a number inserted before the area code when dialing
#         a mobile number from that country from abroad.
#         
#         Arguments:
#         country_code -- the country calling code for which we want the mobile token
#         Returns the mobile token, as a string, for the given country calling code.
#     
#     example_number(region_code)
#         Gets a valid number for the specified region.
#         
#         Arguments:
#         region_code -- The region for which an example number is needed.
#         
#         Returns a valid fixed-line number for the specified region. Returns None
#         when the metadata does not contain such information, or the region 001 is
#         passed in.  For 001 (representing non-geographical numbers), call
#         example_number_for_non_geo_entity instead.
#     
#     example_number_for_non_geo_entity(country_calling_code)
#         Gets a valid number for the specified country calling code for a non-geographical entity.
#         
#         Arguments:
#         country_calling_code -- The country calling code for a non-geographical entity.
#         
#         Returns a valid number for the non-geographical entity. Returns None when
#         the metadata does not contain such information, or the country calling
#         code passed in does not belong to a non-geographical entity.
#     
#     example_number_for_type(region_code, num_type)
#         Gets a valid number for the specified region and number type.
#         
#         If None is given as the region_code, then the returned number object
#         may belong to any country.
#         
#         Arguments:
#         region_code -- The region for which an example number is needed, or None.
#         num_type -- The type of number that is needed.
#         
#         Returns a valid number for the specified region and type. Returns None
#         when the metadata does not contain such information or if an invalid
#         region or region 001 was specified.  For 001 (representing
#         non-geographical numbers), call example_number_for_non_geo_entity instead.
#     
#     expected_cost(numobj)
#         Gets the expected cost category of a short number (however, nothing is
#         implied about its validity). If the country calling code is unique to a
#         region, this method behaves exactly the same as
#         expected_cost_for_region. However, if the country calling code is
#         shared by multiple regions, then it returns the highest cost in the
#         sequence PREMIUM_RATE, UNKNOWN_COST, STANDARD_RATE, TOLL_FREE. The reason
#         for the position of UNKNOWN_COST in this order is that if a number is
#         UNKNOWN_COST in one region but STANDARD_RATE or TOLL_FREE in another, its
#         expected cost cannot be estimated as one of the latter since it might be a
#         PREMIUM_RATE number.
#         
#         For example, if a number is STANDARD_RATE in the US, but TOLL_FREE in
#         Canada, the expected cost returned by this method will be STANDARD_RATE,
#         since the NANPA countries share the same country calling code.
#         
#         Note: If the region from which the number is dialed is known, it is highly preferable to call
#         expected_cost_for_region instead.
#         
#         Arguments:
#         numobj -- the short number for which we want to know the expected cost category
#         
#         Return the highest expected cost category of the short number in the
#         region(s) with the given country calling code
#     
#     expected_cost_for_region(short_numobj, region_dialing_from)
#         Gets the expected cost category of a short number when dialled from a
#         region (however, nothing is implied about its validity). If it is
#         important that the number is valid, then its validity must first be
#         checked using is_valid_short_number_for_region. Note that emergency
#         numbers are always considered toll-free.
#         
#         Example usage:
#         short_number = "110"
#         region_code = "FR"
#         if phonenumbers.is_valid_short_number_for_region(short_number, region_code):
#             cost = phonenumbers.expected_cost(short_number, region_code)  # ShortNumberCost
#             # Do something with the cost information here.
#         
#         Arguments:
#         short_numobj -- the short number for which we want to know the expected cost category
#                   as a PhoneNumber object.
#         region_dialing_from -- the region from which the number is dialed
#         
#         Return the expected cost category for that region of the short
#         number. Returns UNKNOWN_COST if the number does not match a cost
#         category. Note that an invalid number may match any cost category.
#     
#     format_by_pattern(numobj, number_format, user_defined_formats)
#         Formats a phone number using client-defined formatting rules.
#         
#         Note that if the phone number has a country calling code of zero or an
#         otherwise invalid country calling code, we cannot work out things like
#         whether there should be a national prefix applied, or how to format
#         extensions, so we return the national significant number with no
#         formatting applied.
#         
#         Arguments:
#         numobj -- The phone number to be formatted
#         number_format -- The format the phone number should be formatted into,
#                   as a PhoneNumberFormat value.
#         user_defined_formats -- formatting rules specified by clients, as a list
#                   of NumberFormat objects.
#         
#         Returns the formatted phone number.
#     
#     format_in_original_format(numobj, region_calling_from)
#         Format a number using the original format that the number was parsed from.
#         
#         The original format is embedded in the country_code_source field of the
#         PhoneNumber object passed in. If such information is missing, the number
#         will be formatted into the NATIONAL format by default.
#         
#         When  we don't have a formatting pattern for the number, the method
#         returns the raw input when it is available.
#         
#         Note this method guarantees no digit will be inserted, removed or modified
#         as a result of formatting.
#         
#         Arguments:
#         number -- The phone number that needs to be formatted in its original
#                   number format
#         region_calling_from -- The region whose IDD needs to be prefixed if the
#                   original number has one.
#         
#         Returns the formatted phone number in its original number format.
#     
#     format_national_number_with_carrier_code(numobj, carrier_code)
#         Format a number in national format for dialing using the specified carrier.
#         
#         The carrier-code will always be used regardless of whether the phone
#         number already has a preferred domestic carrier code stored. If
#         carrier_code contains an empty string, returns the number in national
#         format without any carrier code.
#         
#         Arguments:
#         numobj -- The phone number to be formatted
#         carrier_code -- The carrier selection code to be used
#         
#         Returns the formatted phone number in national format for dialing using
#         the carrier as specified in the carrier_code.
#     
#     format_national_number_with_preferred_carrier_code(numobj, fallback_carrier_code)
#         Formats a phone number in national format for dialing using the carrier
#         as specified in the preferred_domestic_carrier_code field of the
#         PhoneNumber object passed in. If that is missing, use the
#         fallback_carrier_code passed in instead. If there is no
#         preferred_domestic_carrier_code, and the fallback_carrier_code contains an
#         empty string, return the number in national format without any carrier
#         code.
#         
#         Use format_national_number_with_carrier_code instead if the carrier code
#         passed in should take precedence over the number's
#         preferred_domestic_carrier_code when formatting.
#         
#         Arguments:
#         numobj -- The phone number to be formatted
#         carrier_code -- The carrier selection code to be used, if none is found in the
#                   phone number itself.
#         
#         Returns the formatted phone number in national format for dialing using
#         the number's preferred_domestic_carrier_code, or the fallback_carrier_code
#         pass in if none is found.
#     
#     format_number(numobj, num_format)
#         Formats a phone number in the specified format using default rules.
#         
#         Note that this does not promise to produce a phone number that the user
#         can dial from where they are - although we do format in either 'national'
#         or 'international' format depending on what the client asks for, we do not
#         currently support a more abbreviated format, such as for users in the same
#         "area" who could potentially dial the number without area code. Note that
#         if the phone number has a country calling code of 0 or an otherwise
#         invalid country calling code, we cannot work out which formatting rules to
#         apply so we return the national significant number with no formatting
#         applied.
#         
#         Arguments:
#         numobj -- The phone number to be formatted.
#         num_format -- The format the phone number should be formatted into
#         
#         Returns the formatted phone number.
#     
#     format_number_for_mobile_dialing(numobj, region_calling_from, with_formatting)
#         Returns a number formatted in such a way that it can be dialed from a
#          mobile phone in a specific region.
#         
#         If the number cannot be reached from the region (e.g. some countries block
#         toll-free numbers from being called outside of the country), the method
#         returns an empty string.
#         
#         Arguments:
#         numobj -- The phone number to be formatted
#         region_calling_from -- The region where the call is being placed.
#         
#         with_formatting -- whether the number should be returned with formatting
#                   symbols, such as spaces and dashes.
#         
#         Returns the formatted phone number.
#     
#     format_out_of_country_calling_number(numobj, region_calling_from)
#         Formats a phone number for out-of-country dialing purposes.
#         
#         If no region_calling_from is supplied, we format the number in its
#         INTERNATIONAL format. If the country calling code is the same as that of
#         the region where the number is from, then NATIONAL formatting will be
#         applied.
#         
#         If the number itself has a country calling code of zero or an otherwise
#         invalid country calling code, then we return the number with no formatting
#         applied.
#         
#         Note this function takes care of the case for calling inside of NANPA and
#         between Russia and Kazakhstan (who share the same country calling
#         code). In those cases, no international prefix is used. For regions which
#         have multiple international prefixes, the number in its INTERNATIONAL
#         format will be returned instead.
#         
#         Arguments:
#         numobj -- The phone number to be formatted
#         region_calling_from -- The region where the call is being placed
#         
#         Returns the formatted phone number
#     
#     format_out_of_country_keeping_alpha_chars(numobj, region_calling_from)
#         Formats a phone number for out-of-country dialing purposes.
#         
#         Note that in this version, if the number was entered originally using
#         alpha characters and this version of the number is stored in raw_input,
#         this representation of the number will be used rather than the digit
#         representation. Grouping information, as specified by characters such as
#         "-" and " ", will be retained.
#         
#         Caveats:
#         
#          - This will not produce good results if the country calling code is both
#            present in the raw input _and_ is the start of the national
#            number. This is not a problem in the regions which typically use alpha
#            numbers.
#         
#          - This will also not produce good results if the raw input has any
#            grouping information within the first three digits of the national
#            number, and if the function needs to strip preceding digits/words in
#            the raw input before these digits. Normally people group the first
#            three digits together so this is not a huge problem - and will be fixed
#            if it proves to be so.
#         
#         Arguments:
#         numobj -- The phone number that needs to be formatted.
#         region_calling_from -- The region where the call is being placed.
#         
#         Returns the formatted phone number
#     
#     invalid_example_number(region_code)
#         Gets an invalid number for the specified region.
#         
#         This is useful for unit-testing purposes, where you want to test what
#         will happen with an invalid number. Note that the number that is
#         returned will always be able to be parsed and will have the correct
#         country code. It may also be a valid *short* number/code for this
#         region. Validity checking such numbers is handled with shortnumberinfo.
#         
#         Arguments:
#         region_code -- The region for which an example number is needed.
#         
#         
#         Returns an invalid number for the specified region. Returns None when an
#         unsupported region or the region 001 (Earth) is passed in.
#     
#     is_alpha_number(number)
#         Checks if the number is a valid vanity (alpha) number such as 800
#         MICROSOFT. A valid vanity number will start with at least 3 digits and
#         will have three or more alpha characters. This does not do region-specific
#         checks - to work out if this number is actually valid for a region, it
#         should be parsed and methods such as is_possible_number_with_reason() and
#         is_valid_number() should be used.
#         
#         Arguments:
#         number -- the number that needs to be checked
#         
#         Returns True if the number is a valid vanity number
#     
#     is_carrier_specific(numobj)
#         Given a valid short number, determines whether it is carrier-specific
#         (however, nothing is implied about its validity).  Carrier-specific numbers
#         may connect to a different end-point, or not connect at all, depending
#         on the user's carrier. If it is important that the number is valid, then
#         its validity must first be checked using is_valid_short_number or
#         is_valid_short_number_for_region.
#         
#         Arguments:
#         numobj -- the valid short number to check
#         
#         Returns whether the short number is carrier-specific, assuming the input
#         was a valid short number.
#     
#     is_carrier_specific_for_region(numobj, region_dialing_from)
#         Given a valid short number, determines whether it is carrier-specific when
#         dialed from the given region (however, nothing is implied about its
#         validity). Carrier-specific numbers may connect to a different end-point,
#         or not connect at all, depending on the user's carrier. If it is important
#         that the number is valid, then its validity must first be checked using
#         isValidShortNumber or isValidShortNumberForRegion. Returns false if the
#         number doesn't match the region provided.
#         
#         Arguments:
#         numobj -- the valid short number to check
#         region_dialing_from -- the region from which the number is dialed
#         
#         Returns whether the short number is carrier-specific, assuming the input
#         was a valid short number.
#     
#     is_emergency_number(number, region_code)
#         Returns true if the given number exactly matches an emergency service
#         number in the given region.
#         
#         This method takes into account cases where the number might contain
#         formatting, but doesn't allow additional digits to be appended.  Note that
#         is_emergency_number(number, region) implies
#         connects_to_emergency_number(number, region).
#         
#         Arguments:
#         number -- The phone number to test.
#         region_code -- The region where the phone number is being dialed.
#         
#         Returns if the number exactly matches an emergency services number in the
#         given region.
#     
#     is_mobile_number_portable_region(region_code)
#         Returns true if the supplied region supports mobile number portability.
#         Returns false for invalid, unknown or regions that don't support mobile
#         number portability.
#         
#         Arguments:
#         region_code -- the region for which we want to know whether it supports mobile number
#                        portability or not.
#     
#     is_nanpa_country(region_code)
#         Checks if this region is a NANPA region.
#         
#         Returns True if region_code is one of the regions under the North American
#         Numbering Plan Administration (NANPA).
#     
#     is_number_geographical(numobj)
#         Tests whether a phone number has a geographical association.
#         
#         It checks if the number is associated with a certain region in the country
#         to which it belongs. Note that this doesn't verify if the number is
#         actually in use.
#         country_code -- the country calling code for which we want the mobile token
#     
#     is_number_match(num1, num2)
#         Takes two phone numbers and compares them for equality.
#         
#         For example, the numbers +1 345 657 1234 and 657 1234 are a SHORT_NSN_MATCH.
#         The numbers +1 345 657 1234 and 345 657 are a NO_MATCH.
#         
#         Arguments
#         num1 -- First number object or string to compare. Can contain formatting,
#                   and can have country calling code specified with + at the start.
#         num2 -- Second number object or string to compare. Can contain formatting,
#                   and can have country calling code specified with + at the start.
#         
#         Returns:
#          - EXACT_MATCH if the country_code, NSN, presence of a leading zero for
#            Italian numbers and any extension present are the same.
#          - NSN_MATCH if either or both has no region specified, and the NSNs and
#            extensions are the same.
#          - SHORT_NSN_MATCH if either or both has no region specified, or the
#            region specified is the same, and one NSN could be a shorter version of
#            the other number. This includes the case where one has an extension
#            specified, and the other does not.
#          - NO_MATCH otherwise.
#     
#     is_number_type_geographical(num_type, country_code)
#         Tests whether a phone number has a geographical association,
#         as represented by its type and the country it belongs to.
#         
#         This version of isNumberGeographical exists since calculating the phone
#         number type is expensive; if we have already done this, we don't want to
#         do it again.
#     
#     is_possible_number(numobj)
#         Convenience wrapper around is_possible_number_with_reason.
#         
#         Instead of returning the reason for failure, this method returns true if
#         the number is either a possible fully-qualified number (containing the area
#         code and country code), or if the number could be a possible local number
#         (with a country code, but missing an area code). Local numbers are
#         considered possible if they could be possibly dialled in this format: if
#         the area code is needed for a call to connect, the number is not considered
#         possible without it.
#         
#         Arguments:
#         numobj -- the number object that needs to be checked
#         
#         Returns True if the number is possible
#     
#     is_possible_number_for_type(numobj, numtype)
#         Convenience wrapper around is_possible_number_for_type_with_reason.
#         
#         Instead of returning the reason for failure, this method returns true if
#         the number is either a possible fully-qualified number (containing the area
#         code and country code), or if the number could be a possible local number
#         (with a country code, but missing an area code). Local numbers are
#         considered possible if they could be possibly dialled in this format: if
#         the area code is needed for a call to connect, the number is not considered
#         possible without it.
#         
#         Arguments:
#         numobj -- the number object that needs to be checked
#         numtype -- the type we are interested in
#         
#         Returns True if the number is possible
#     
#     is_possible_number_for_type_with_reason(numobj, numtype)
#         Check whether a phone number is a possible number of a particular type.
#         
#         For types that don't exist in a particular region, this will return a result
#         that isn't so useful; it is recommended that you use
#         supported_types_for_region or supported_types_for_non_geo_entity
#         respectively before calling this method to determine whether you should call
#         it for this number at all.
#         
#         This provides a more lenient check than is_valid_number in the following sense:
#         
#          - It only checks the length of phone numbers. In particular, it doesn't
#            check starting digits of the number.
#         
#          - For some numbers (particularly fixed-line), many regions have the
#            concept of area code, which together with subscriber number constitute
#            the national significant number. It is sometimes okay to dial only the
#            subscriber number when dialing in the same area. This function will
#            return IS_POSSIBLE_LOCAL_ONLY if the subscriber-number-only version is
#            passed in. On the other hand, because is_valid_number validates using
#            information on both starting digits (for fixed line numbers, that would
#            most likely be area codes) and length (obviously includes the length of
#            area codes for fixed line numbers), it will return false for the
#            subscriber-number-only version.
#         
#         Arguments:
#         numobj -- The number object that needs to be checked
#         numtype -- The type we are interested in
#         
#         Returns a value from ValidationResult which indicates whether the number
#         is possible
#     
#     is_possible_number_string(number, region_dialing_from)
#         Check whether a phone number string is a possible number.
#         
#         Takes a number in the form of a string, and the region where the number
#         could be dialed from. It provides a more lenient check than
#         is_valid_number; see is_possible_number_with_reason() for details.
#         
#         This method first parses the number, then invokes is_possible_number with
#         the resultant PhoneNumber object.
#         
#         Arguments:
#         number -- The number that needs to be checked, in the form of a string.
#         region_dialling_from -- The region that we are expecting the number to be
#                   dialed from.  Note this is different from the region where the
#                   number belongs.  For example, the number +1 650 253 0000 is a
#                   number that belongs to US. When written in this form, it can be
#                   dialed from any region. When it is written as 00 1 650 253 0000,
#                   it can be dialed from any region which uses an international
#                   dialling prefix of 00. When it is written as 650 253 0000, it
#                   can only be dialed from within the US, and when written as 253
#                   0000, it can only be dialed from within a smaller area in the US
#                   (Mountain View, CA, to be more specific).
#         
#         Returns True if the number is possible
#     
#     is_possible_number_with_reason(numobj)
#     
#     is_possible_short_number(numobj)
#         Check whether a short number is a possible number.
#         
#         If a country calling code is shared by multiple regions, this returns True
#         if it's possible in any of them. This provides a more lenient check than
#         is_valid_short_number.
#         
#         Arguments:
#         numobj -- the short number to check
#         
#         Return whether the number is a possible short number.
#     
#     is_possible_short_number_for_region(short_numobj, region_dialing_from)
#         Check whether a short number is a possible number when dialled from a
#         region. This provides a more lenient check than
#         is_valid_short_number_for_region.
#         
#         Arguments:
#         short_numobj -- the short number to check as a PhoneNumber object.
#         region_dialing_from -- the region from which the number is dialed
#         
#         Return whether the number is a possible short number.
#     
#     is_sms_service_for_region(numobj, region_dialing_from)
#         Given a valid short number, determines whether it is an SMS service
#         (however, nothing is implied about its validity). An SMS service is where
#         the primary or only intended usage is to receive and/or send text messages
#         (SMSs). This includes MMS as MMS numbers downgrade to SMS if the other
#         party isn't MMS-capable. If it is important that the number is valid, then
#         its validity must first be checked using is_valid_short_number or
#         is_valid_short_number_for_region.  Returns False if the number doesn't
#         match the region provided.
#         
#         Arguments:
#         numobj -- the valid short number to check
#         region_dialing_from -- the region from which the number is dialed
#         
#         Returns whether the short number is an SMS service in the provided region,
#         assuming the input was a valid short number.
#     
#     is_valid_number(numobj)
#         Tests whether a phone number matches a valid pattern.
#         
#         Note this doesn't verify the number is actually in use, which is
#         impossible to tell by just looking at a number itself.  It only verifies
#         whether the parsed, canonicalised number is valid: not whether a
#         particular series of digits entered by the user is diallable from the
#         region provided when parsing. For example, the number +41 (0) 78 927 2696
#         can be parsed into a number with country code "41" and national
#         significant number "789272696". This is valid, while the original string
#         is not diallable.
#         
#         Arguments:
#         numobj -- The phone number object that we want to validate
#         
#         Returns a boolean that indicates whether the number is of a valid pattern.
#     
#     is_valid_number_for_region(numobj, region_code)
#         Tests whether a phone number is valid for a certain region.
#         
#         Note this doesn't verify the number is actually in use, which is
#         impossible to tell by just looking at a number itself. If the country
#         calling code is not the same as the country calling code for the region,
#         this immediately exits with false. After this, the specific number pattern
#         rules for the region are examined. This is useful for determining for
#         example whether a particular number is valid for Canada, rather than just
#         a valid NANPA number.
#         
#         Warning: In most cases, you want to use is_valid_number instead. For
#         example, this method will mark numbers from British Crown dependencies
#         such as the Isle of Man as invalid for the region "GB" (United Kingdom),
#         since it has its own region code, "IM", which may be undesirable.
#         
#         Arguments:
#         numobj -- The phone number object that we want to validate.
#         region_code -- The region that we want to validate the phone number for.
#         
#         Returns a boolean that indicates whether the number is of a valid pattern.
#     
#     is_valid_short_number(numobj)
#         Tests whether a short number matches a valid pattern.
#         
#         If a country calling code is shared by multiple regions, this returns True
#         if it's valid in any of them. Note that this doesn't verify the number is
#         actually in use, which is impossible to tell by just looking at the number
#         itself. See is_valid_short_number_for_region for details.
#         
#         Arguments:
#         numobj - the short number for which we want to test the validity
#         
#         Return whether the short number matches a valid pattern
#     
#     is_valid_short_number_for_region(short_numobj, region_dialing_from)
#         Tests whether a short number matches a valid pattern in a region.
#         
#         Note that this doesn't verify the number is actually in use, which is
#         impossible to tell by just looking at the number itself.
#         
#         Arguments:
#         short_numobj -- the short number to check as a PhoneNumber object.
#         region_dialing_from -- the region from which the number is dialed
#         
#         Return whether the short number matches a valid pattern
#     
#     length_of_geographical_area_code(numobj)
#         Return length of the geographical area code for a number.
#         
#         Gets the length of the geographical area code from the PhoneNumber object
#         passed in, so that clients could use it to split a national significant
#         number into geographical area code and subscriber number. It works in such
#         a way that the resultant subscriber number should be diallable, at least
#         on some devices. An example of how this could be used:
#         
#         >>> import phonenumbers
#         >>> numobj = phonenumbers.parse("16502530000", "US")
#         >>> nsn = phonenumbers.national_significant_number(numobj)
#         >>> ac_len = phonenumbers.length_of_geographical_area_code(numobj)
#         >>> if ac_len > 0:
#         ...     area_code = nsn[:ac_len]
#         ...     subscriber_number = nsn[ac_len:]
#         ... else:
#         ...     area_code = ""
#         ...     subscriber_number = nsn
#         
#         N.B.: area code is a very ambiguous concept, so the I18N team generally
#         recommends against using it for most purposes, but recommends using the
#         more general national_number instead. Read the following carefully before
#         deciding to use this method:
#         
#          - geographical area codes change over time, and this method honors those
#            changes; therefore, it doesn't guarantee the stability of the result it
#            produces.
#          - subscriber numbers may not be diallable from all devices (notably
#            mobile devices, which typically require the full national_number to be
#            dialled in most countries).
#          - most non-geographical numbers have no area codes, including numbers
#            from non-geographical entities.
#          - some geographical numbers have no area codes.
#         
#         Arguments:
#         numobj -- The PhoneNumber object to find the length of the area code form.
#         
#         Returns the length of area code of the PhoneNumber object passed in.
#     
#     length_of_national_destination_code(numobj)
#         Return length of the national destination code code for a number.
#         
#         Gets the length of the national destination code (NDC) from the
#         PhoneNumber object passed in, so that clients could use it to split a
#         national significant number into NDC and subscriber number. The NDC of a
#         phone number is normally the first group of digit(s) right after the
#         country calling code when the number is formatted in the international
#         format, if there is a subscriber number part that follows.
#         
#         N.B.: similar to an area code, not all numbers have an NDC!
#         
#         An example of how this could be used:
#         
#         >>> import phonenumbers
#         >>> numobj = phonenumbers.parse("18002530000", "US")
#         >>> nsn = phonenumbers.national_significant_number(numobj)
#         >>> ndc_len = phonenumbers.length_of_national_destination_code(numobj)
#         >>> if ndc_len > 0:
#         ...     national_destination_code = nsn[:ndc_len]
#         ...     subscriber_number = nsn[ndc_len:]
#         ... else:
#         ...     national_destination_code = ""
#         ...     subscriber_number = nsn
#         
#         Refer to the unittests to see the difference between this function and
#         length_of_geographical_area_code.
#         
#         Arguments:
#         numobj -- The PhoneNumber object to find the length of the NDC from.
#         
#         Returns the length of NDC of the PhoneNumber object passed in, which
#         could be zero.
#     
#     national_significant_number(numobj)
#         Gets the national significant number of a phone number.
#         
#         Note that a national significant number doesn't contain a national prefix
#         or any formatting.
#         
#         Arguments:
#         numobj -- The PhoneNumber object for which the national significant number
#                   is needed.
#         
#         Returns the national significant number of the PhoneNumber object passed
#         in.
#     
#     ndd_prefix_for_region(region_code, strip_non_digits)
#         Returns the national dialling prefix for a specific region.
#         
#         For example, this would be 1 for the United States, and 0 for New
#         Zealand. Set strip_non_digits to True to strip symbols like "~" (which
#         indicates a wait for a dialling tone) from the prefix returned. If no
#         national prefix is present, we return None.
#         
#         Warning: Do not use this method for do-your-own formatting - for some
#         regions, the national dialling prefix is used only for certain types of
#         numbers. Use the library's formatting functions to prefix the national
#         prefix when required.
#         
#         Arguments:
#         region_code -- The region that we want to get the dialling prefix for.
#         strip_non_digits -- whether to strip non-digits from the national
#                    dialling prefix.
#         
#         Returns the dialling prefix for the region denoted by region_code.
#     
#     normalize_diallable_chars_only(number)
#         Normalizes a string of characters representing a phone number.
#         
#         This strips all characters which are not diallable on a mobile phone
#         keypad (including all non-ASCII digits).
#         
#         Arguments:
#         number -- a string of characters representing a phone number
#         
#         Returns the normalized string version of the phone number.
#     
#     normalize_digits_only(number, keep_non_digits=False)
#         Normalizes a string of characters representing a phone number.
#         
#         This converts wide-ascii and arabic-indic numerals to European numerals,
#         and strips punctuation and alpha characters (optional).
#         
#         Arguments:
#         number -- a string representing a phone number
#         keep_non_digits -- whether to keep non-digits
#         
#         Returns the normalized string version of the phone number.
#     
#     number_type(numobj)
#         Gets the type of a valid phone number.
#         
#         Arguments:
#         numobj -- The PhoneNumber object that we want to know the type of.
#         
#         Returns the type of the phone number, as a PhoneNumberType value;
#         returns PhoneNumberType.UNKNOWN if it is invalid.
#     
#     parse(number, region=None, keep_raw_input=False, numobj=None, _check_region=True)
#         Parse a string and return a corresponding PhoneNumber object.
#         
#         The method is quite lenient and looks for a number in the input text
#         (raw input) and does not check whether the string is definitely only a
#         phone number. To do this, it ignores punctuation and white-space, as
#         well as any text before the number (e.g. a leading "Tel: ") and trims
#         the non-number bits.  It will accept a number in any format (E164,
#         national, international etc), assuming it can be interpreted with the
#         defaultRegion supplied. It also attempts to convert any alpha characters
#         into digits if it thinks this is a vanity number of the type "1800
#         MICROSOFT".
#         
#         This method will throw a NumberParseException if the number is not
#         considered to be a possible number. Note that validation of whether the
#         number is actually a valid number for a particular region is not
#         performed. This can be done separately with is_valid_number.
#         
#         Note this method canonicalizes the phone number such that different
#         representations can be easily compared, no matter what form it was
#         originally entered in (e.g. national, international). If you want to
#         record context about the number being parsed, such as the raw input that
#         was entered, how the country code was derived etc. then ensure
#         keep_raw_input is set.
#         
#         Note if any new field is added to this method that should always be filled
#         in, even when keep_raw_input is False, it should also be handled in the
#         _copy_core_fields_only() function.
#         
#         Arguments:
#         number -- The number that we are attempting to parse. This can
#                   contain formatting such as +, ( and -, as well as a phone
#                   number extension. It can also be provided in RFC3966 format.
#         region -- The region that we are expecting the number to be from. This
#                   is only used if the number being parsed is not written in
#                   international format. The country_code for the number in
#                   this case would be stored as that of the default region
#                   supplied. If the number is guaranteed to start with a '+'
#                   followed by the country calling code, then None or
#                   UNKNOWN_REGION can be supplied.
#         keep_raw_input -- Whether to populate the raw_input field of the
#                   PhoneNumber object with number (as well as the
#                   country_code_source field).
#         numobj -- An optional existing PhoneNumber object to receive the
#                   parsing results
#         _check_region -- Whether to check the supplied region parameter;
#                   should always be True for external callers.
#         
#         Returns a PhoneNumber object filled with the parse number.
#         
#         Raises:
#         NumberParseException if the string is not considered to be a viable
#         phone number (e.g.  too few or too many digits) or if no default
#         region was supplied and the number is not in international format
#         (does not start with +).
#     
#     region_code_for_country_code(country_code)
#         Returns the region code that matches a specific country calling code.
#         
#         In the case of no region code being found, UNKNOWN_REGION ('ZZ') will be
#         returned. In the case of multiple regions, the one designated in the
#         metadata as the "main" region for this calling code will be returned.  If
#         the country_code entered is valid but doesn't match a specific region
#         (such as in the case of non-geographical calling codes like 800) the value
#         "001" will be returned (corresponding to the value for World in the UN
#         M.49 schema).
#     
#     region_code_for_number(numobj)
#         Returns the region where a phone number is from.
#         
#         This could be used for geocoding at the region level. Only guarantees
#         correct results for valid, full numbers (not short-codes, or invalid
#         numbers).
#         
#         Arguments:
#         numobj -- The phone number object whose origin we want to know
#         
#         Returns the region where the phone number is from, or None if no region
#         matches this calling code.
#     
#     region_codes_for_country_code(country_code)
#         Returns a list with the region codes that match the specific country calling code.
#         
#         For non-geographical country calling codes, the region code 001 is
#         returned. Also, in the case of no region code being found, an empty
#         list is returned.
#     
#     supported_calling_codes()
#         Returns all country calling codes the library has metadata for, covering
#         both non-geographical entities (global network calling codes) and those
#         used for geographical entities. This could be used to populate a drop-down
#         box of country calling codes for a phone-number widget, for instance.
#         
#         Returns an unordered set of the country calling codes for every geographica
#         and non-geographical entity the library supports.
#     
#     supported_types_for_non_geo_entity(country_code)
#         Returns the types for a country-code belonging to a non-geographical entity
#         which the library has metadata for. Will not include FIXED_LINE_OR_MOBILE
#         (if numbers for this non-geographical entity could be classified as
#         FIXED_LINE_OR_MOBILE, both FIXED_LINE and MOBILE would be present) and
#         UNKNOWN.
#         
#         No types will be returned for country calling codes that do not map to a
#         known non-geographical entity.
#     
#     supported_types_for_region(region_code)
#         Returns the types for a given region which the library has metadata for.
#         
#         Will not include FIXED_LINE_OR_MOBILE (if numbers in this region could
#         be classified as FIXED_LINE_OR_MOBILE, both FIXED_LINE and MOBILE would
#         be present) and UNKNOWN.
#         
#         No types will be returned for invalid or unknown region codes.
#     
#     truncate_too_long_number(numobj)
#         Truncate a number object that is too long.
#         
#         Attempts to extract a valid number from a phone number that is too long
#         to be valid, and resets the PhoneNumber object passed in to that valid
#         version. If no valid number could be extracted, the PhoneNumber object
#         passed in will not be modified.
#         
#         Arguments:
#         numobj -- A PhoneNumber object which contains a number that is too long to
#                   be valid.
#         
#         Returns True if a valid phone number can be successfully extracted.
# 
# DATA
#     COUNTRY_CODES_FOR_NON_GEO_REGIONS = {800, 808, 870, 878, 881, 882, ......
#     COUNTRY_CODE_TO_REGION_CODE = {1: ('US', 'AG', 'AI', 'AS', 'BB', 'BM',...
#     NON_DIGITS_PATTERN = re.compile('(?:\\D+)')
#     REGION_CODE_FOR_NON_GEO_ENTITY = '001'
#     SUPPORTED_REGIONS = {'AC', 'AD', 'AE', 'AF', 'AG', 'AI', ...}
#     SUPPORTED_SHORT_REGIONS = ['AC', 'AD', 'AE', 'AF', 'AG', 'AI', 'AL', '...
#     UNKNOWN_REGION = 'ZZ'
#     __all__ = ['PhoneNumber', 'CountryCodeSource', 'FrozenPhoneNumber', 'R...
# 
# VERSION
#     8.12.43
# 
# FILE
#     c:\users\jean\appdata\roaming\python\python310\site-packages\phonenumbers\__init__.py

