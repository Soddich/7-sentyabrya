class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, *memories):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = list(memories[:4])

    def get_config(self):
        mem_data = []

        for mem in self.mem_slots:
            mem_data.append(mem.name + " - " + str(mem.volume))

        return [
            "Материнская плата: " + self.name,
            "Центральный процессор: " + self.cpu.name + ", " + str(self.cpu.fr),
            "Слотов памяти: " + str(self.total_mem_slots),
            "Память: " + "; ".join(mem_data)
        ]

cpu = CPU('SuperCPU', 1200)
mem1 = Memory('Kingston', 16)
mem2 = Memory('Samsung', 4)

mb = MotherBoard('Mamka', cpu, mem1, mem2)

print(mb.get_config())