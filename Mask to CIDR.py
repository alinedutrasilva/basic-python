def mask_to_cidr(mask):
    #Split into 4 octets
    mask = mask.split(".")
    cidr = 0
    #Data validation
    my_val_list = ["0", "128", "192", "224", "240", "248", "252", "254", "255"]
    for i in range(0,4):
        if len(mask) == 4 and mask[i] in my_val_list:
            mask[i] = "{0:b}".format(int(mask[i])) #Converting into binary as string
            for ix in mask[i]:
                if ix == "1":
                    cidr += 1 #Counting the bits
        else:
            return "INVALID MASK!"
    return "/" + str(cidr)

if __name__ == "__main__":
    mask = "255.255.255.0"
    mask_to_cidr(mask)
    print(mask_to_cidr(mask))