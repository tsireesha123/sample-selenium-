def simple_materials(area_sq_yards):
    # Convert to square feet
    sq_ft = area_sq_yards * 9
    
    # Assume thickness of concrete slab = 0.5 feet (6 inches)
    volume1= sq_ft * 0.5  # in cubic feet
    
    # Convert to cubic meters
    volume2 = volume1 / 35.31
    
    # Estimate materials for M20 concrete mix
    cement = volume2 * 5.24   # approx 5.24 bags per m3
    sand = volume2 * 0.273     # sand in cubic meters
    iron = (sq_ft * 4) / 1000    # 4 kg per sq ft
    return {
        "Cement": round(cement),
        "Sand": round(sand, 2),
        "Iron": round(iron, 2)
    }
print(simple_materials(200))
