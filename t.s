                .data
error_op:       .asciiz     "Error opening the file"
ok_message:     .asciiz     "All right"
params_sys1:    .asciiz     "filename.txt"
                .word64     0xF

                .text
open:           daddi       r14, r0, params_sys1
                syscall     1
                daddi       $s0, r0, -1
                dadd        $s2, r0, r1
                daddi       $a0,r0,ok_message
                bne         r1,$s0,end
                daddi       $a0,r0,error_op

end:            jal         print_string
                syscall 0

                #include    print.s