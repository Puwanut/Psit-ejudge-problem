"""BloodDonation"""
def can_donate(age, weight, times_donate):
    """Return Yes if can donate"""
    if age < 17 or age > 70:
        return 'No'
    if age == 17 or 60 <= age <= 70:
        book = input()
        if book == 'False':
            return 'No'
    if weight < 45 or (age > 55 and times_donate == 0):
        return 'No'
    return 'Yes'
print(can_donate(int(input()), int(input()), int(input())))
