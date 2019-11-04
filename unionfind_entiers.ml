(** Structure d'ensembles disjoints, structure dite Union-Find

    - Uniquement pour des ensembles d'entiers.
    - Note: pour des tout petits entiers, on peut faire bien mieux,
      en représentant {i} comme 2^i, {i} u {i} = 2^i + 2^j etc.

    @author Lilian Besson <lilian.besson[AT]ens-cachan.fr>
*)


(** {6 Implémentation pour des données entières uniquement, sans foncteur } *)

module EnsemblesDisjointsEntiers = struct
    (** Type interne pour un pointeur *)
    type t = {
        valeur: int;
        mutable rang: int;
        mutable parent: t option
    }

    (** Crée un singleton contenant x. *)
    let singleton x =
        {valeur = x; rang = 0; parent = None}

    (** Renvoie le représentant de la classe d'équivalence de x.
        Utilise l'optimisation dite de compression des chemins.

        Complexité : en [O(alpha(n))].
      *)
    let rec trouver x =
        match x.parent with
            | None -> x
            | Some(y) -> begin
                x.parent <- Some(trouver y);
                y
            end

    (** Unie les deux classes d'équivalence de x et y.
        Utilise l'optimisation dite de l'union équilibrée.

        Complexité : en [O(alpha(n))].
      *)
    let union x y =
        let xr = trouver x and yr = trouver y in
        if xr != yr then (
            if xr.rang < yr.rang then
                xr.parent <- Some(yr)
            else (
                if xr.rang > yr.rang then
                    yr.parent <- Some(xr)
                else (
                    yr.parent <- Some(xr);
                    xr.rang <- xr.rang + 1
                )
            )
        )
end ;;


(** {6 Exemples} *)

module S = EnsemblesDisjointsEntiers;;

let s1 = S.singleton 1
and s2 = S.singleton 2
and s3 = S.singleton 3
and s4 = S.singleton 4
and s5 = S.singleton 5;;

S.union s1 s2;;
S.union s4 s5;;
S.union s2 s3;;
S.union s3 s1;;

s1;;
s2;;
s3;;
s4;;
s5;;
