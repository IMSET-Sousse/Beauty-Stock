import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"

export function RecentSales() {
  return (
    <div className="space-y-8">
      <div className="flex items-center">
        <Avatar className="h-9 w-9">
          <AvatarImage src="/placeholder-user.jpg" alt="Avatar" />
          <AvatarFallback>SC</AvatarFallback>
        </Avatar>
        <div className="ml-4 space-y-1">
          <p className="text-sm font-medium leading-none">Sophie Cosmetique</p>
          <p className="text-sm text-muted-foreground">Purchased 12 items</p>
        </div>
        <div className="ml-auto font-medium">+$1,248.00</div>
      </div>
      <div className="flex items-center">
        <Avatar className="h-9 w-9">
          <AvatarImage src="/placeholder-user.jpg" alt="Avatar" />
          <AvatarFallback>JL</AvatarFallback>
        </Avatar>
        <div className="ml-4 space-y-1">
          <p className="text-sm font-medium leading-none">Jackson Luxury</p>
          <p className="text-sm text-muted-foreground">Purchased 5 items</p>
        </div>
        <div className="ml-auto font-medium">+$546.80</div>
      </div>
      <div className="flex items-center">
        <Avatar className="h-9 w-9">
          <AvatarImage src="/placeholder-user.jpg" alt="Avatar" />
          <AvatarFallback>BG</AvatarFallback>
        </Avatar>
        <div className="ml-4 space-y-1">
          <p className="text-sm font-medium leading-none">Beauty Gallery</p>
          <p className="text-sm text-muted-foreground">Purchased 8 items</p>
        </div>
        <div className="ml-auto font-medium">+$892.50</div>
      </div>
      <div className="flex items-center">
        <Avatar className="h-9 w-9">
          <AvatarImage src="/placeholder-user.jpg" alt="Avatar" />
          <AvatarFallback>ES</AvatarFallback>
        </Avatar>
        <div className="ml-4 space-y-1">
          <p className="text-sm font-medium leading-none">Elegant Spa</p>
          <p className="text-sm text-muted-foreground">Purchased 3 items</p>
        </div>
        <div className="ml-auto font-medium">+$298.00</div>
      </div>
      <div className="flex items-center">
        <Avatar className="h-9 w-9">
          <AvatarImage src="/placeholder-user.jpg" alt="Avatar" />
          <AvatarFallback>GS</AvatarFallback>
        </Avatar>
        <div className="ml-4 space-y-1">
          <p className="text-sm font-medium leading-none">Glamour Salon</p>
          <p className="text-sm text-muted-foreground">Purchased 6 items</p>
        </div>
        <div className="ml-auto font-medium">+$432.00</div>
      </div>
    </div>
  )
}
