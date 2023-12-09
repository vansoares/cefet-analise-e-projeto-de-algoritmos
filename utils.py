

def calculate_bin_content(bin):
    bin_content = 0
    for i in bin:
        bin_content += i[0]

    return bin_content

def get_total_waste(bins, capacity):
    waste = 0
    for b in bins:
        bin_content = calculate_bin_content(b)
        waste += capacity - bin_content
    return waste