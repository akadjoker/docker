import pyopencl as cl
import numpy as np

# Configurar plataforma e dispositivo
platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
context = cl.Context([device])
queue = cl.CommandQueue(context)

# Dados para o kernel
a = np.array([1, 2, 3, 4], dtype=np.float32)
b = np.array([5, 6, 7, 8], dtype=np.float32)
result = np.empty_like(a)

# Criar buffers
mf = cl.mem_flags
a_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a)
b_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b)
res_buf = cl.Buffer(context, mf.WRITE_ONLY, result.nbytes)

# Escrever o kernel
kernel_code = """
__kernel void add(
    __global const float *a,
    __global const float *b,
    __global float *result)
{
    int gid = get_global_id(0);
    result[gid] = a[gid] + b[gid];
}
"""
program = cl.Program(context, kernel_code).build()

# Executar o kernel
program.add(queue, a.shape, None, a_buf, b_buf, res_buf)
cl.enqueue_copy(queue, result, res_buf)

print("Resultado:", result)

