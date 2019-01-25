long long n;
int count = 0;
print("Enter an integer: ");
scanf("%lld", &n);
while(n != 0)
{
 n = n/10
 n /= 10;  
 ++count;
 }
 print("Number of digits: %d", count);
}
