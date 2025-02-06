#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/neutrino.h>
#include <sys/rpi_gpio.h>

int
main(int argc, char **argv)
{
    int fd = open("/dev/gpio/msg", O_RDWR);
    if (fd == -1)
    {
        perror("open");
        return EXIT_FAILURE;
    }

    rpi_gpio_msg_t msg =
    {
        .hdr.type = _IO_MSG,
        .hdr.subtype = RPI_GPIO_SET_SELECT,
        .hdr.mgrid = RPI_GPIO_IOMGR,
        .gpio = 16,
        .value = RPI_GPIO_FUNC_OUT
    };

    if (MsgSend(fd, &msg, sizeof(msg), NULL, 0) == -1)
    {
        perror("MsgSend(output)");
        return EXIT_FAILURE;
    }

    msg.hdr.subtype = RPI_GPIO_WRITE;
    msg.value = 1;

    if (MsgSend(fd, &msg, sizeof(msg), NULL, 0) == -1)
    {
        perror("MsgSend(output)");
        return EXIT_FAILURE;
    }

    usleep(5000000);

    msg.value = 0;

    if (MsgSend(fd, &msg, sizeof(msg), NULL, 0) == -1)
    {
        perror("MsgSend(output)");
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
