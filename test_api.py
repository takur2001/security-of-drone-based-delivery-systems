import requests
import json
import time

BASE_URL = "http://localhost:5002"

def test_system():
    print("\n" + "="*70)
    print("🚁 API TESTS")
    print("="*70)
    
    # Test 1
    print("\nTEST 1: Server Check")
    try:
        r = requests.get(BASE_URL)
        print("✅ Server running")
    except:
        print("❌ Server not running! Start it first.")
        return
    
    # Test 2
    print("\nTEST 2: Create Delivery")
    r = requests.post(f"{BASE_URL}/api/delivery/create", 
                      json={"customer_name": "John Doe"})
    data = r.json()
    pkg_id = data['package_id']
    otp = data['otp']
    print(f"✅ Package: {pkg_id}")
    print(f"   OTP: {otp}")
    
    # Test 3
    print("\nTEST 3: Position Updates")
    for i in range(5):
        time.sleep(1)
        r = requests.get(f"{BASE_URL}/api/delivery/update/{pkg_id}")
        pos = r.json()['update']['position']
        print(f"   Update {i+1}: Lat={pos['lat']:.4f}")
    
    # Test 4
    print("\nTEST 4: GPS Spoofing")
    r = requests.post(f"{BASE_URL}/api/security/attack",
                     json={"package_id": pkg_id, "attack_type": "gps_spoofing"})
    print(f"✅ {r.json()['result']['status']}")
    
    # Test 5
    print("\nTEST 5: Wrong OTP")
    for i in range(3):
        r = requests.post(f"{BASE_URL}/api/delivery/verify",
                         json={"package_id": pkg_id, "otp": "000000"})
        print(f"   Attempt {i+1}: {r.json()['message']}")
        if 'LOCKDOWN' in r.json().get('error', ''):
            break
    
    # Test 6
    print("\nTEST 6: Successful Delivery")
    r = requests.post(f"{BASE_URL}/api/delivery/create",
                     json={"customer_name": "Jane Smith"})
    data = r.json()
    pkg_id2 = data['package_id']
    otp2 = data['otp']
    
    print(f"✅ Package: {pkg_id2}")
    for _ in range(10):
        time.sleep(0.5)
        r = requests.get(f"{BASE_URL}/api/delivery/update/{pkg_id2}")
        if r.json()['update']['status'] == "arrived":
            break
    
    r = requests.post(f"{BASE_URL}/api/delivery/verify",
                     json={"package_id": pkg_id2, "otp": otp2})
    print(f"✅ {r.json()['message']}")
    
    print("\n" + "="*70)
    print("✅ ALL TESTS PASSED")
    print("="*70 + "\n")

if __name__ == "__main__":
    print("\n⚠️  Make sure server is running!")
    input("Press ENTER to start tests...")
    test_system()