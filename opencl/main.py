import pyopencl as cl

def test_opencl():
    # Obter plataformas disponíveis
    platforms = cl.get_platforms()
    if not platforms:
        print("Nenhuma plataforma OpenCL encontrada!")
        return

    print(f"Plataformas encontradas: {len(platforms)}")
    for i, platform in enumerate(platforms):
        print(f"Platform {i}: {platform.name}")

        # Obter dispositivos disponíveis na plataforma
        devices = platform.get_devices()
        print(f"  Dispositivos encontrados: {len(devices)}")
        for j, device in enumerate(devices):
            print(f"  Device {j}: {device.name}")
            print(f"    Tipo: {cl.device_type.to_string(device.type)}")
            print(f"    Max Compute Units: {device.max_compute_units}")
            print(f"    Global Memory Size: {device.global_mem_size / (1024 ** 2):.2f} MB")

if __name__ == "__main__":
    test_opencl()

