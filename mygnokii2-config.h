#ifndef config_h
#define config_h

/* This is config file. Change ONLY lines with comment */

#define VERSION "0.45"			/* Version of package 		*/

#ifndef _MSC_VER
#  define DEBUG				/* Want DEBUG info or not ?	*/
#endif

#define GSM_ENABLE_MBUS2		/* MBUS2 over cable 		*/
#define GSM_ENABLE_FBUS2		/* FBUS2 over cable. 		*/
#define GSM_ENABLE_DLR3			/* DLR3 cable			*/
#define GSM_ENABLE_IRDA			/* Direct infrared		*/
#define GSM_ENABLE_INFRARED		/* Infrared over irda sockets	*/
#define GSM_ENABLE_AT			/* AT protocol			*/

/* By default commented: some people reported me (for example, with 6210
 * and 3210), that their phones doesn't answer at all sometimes or answer
 * with (too) long delay. Possible reason: firmware in phone is too slow
 * I didn't have such problems personally with phone and PC with Celeron 800
 * Please also note, that CB function was always TO CHECK in mygnokii/gnokii
 * too.
 */
#define GSM_ENABLE_CELLBROADCAST	/* Enables cell broadcast	*/

/* By default commented: you can have some problems, when using it.
 * Example: with my 6210 after using it info about incoming sms is shown much
 * earlier than sms in phone and phone restart (once and random) later after
 * connection. Seems phone firmware isn't too good here
 */
//#define GSM_ENABLE_N71_91INCOMINGSMS	/* Show incoming SMSfor7110/9110*/

#define GSM_ENABLE_NOKIA6110		/* n6110.c models		*/
#define GSM_ENABLE_NOKIA6510		/* n6510.c (DCT4) models	*/
#define GSM_ENABLE_NOKIA7110		/* n7110.c models		*/
#define GSM_ENABLE_NOKIA9110		/* n9110.c models		*/
#define GSM_ENABLE_ATGEN		/* AT generic models		*/

/* Bu default commented: some parts of source (especially for DCT4) are not
 * ready or not tested at all (or aren't good tested). Uncomment, if want them
 */
#define DEVELOP

#endif
